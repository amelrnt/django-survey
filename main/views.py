from django import forms
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from django_tables2.views import SingleTableMixin

from .filters import AspectFilter
from .forms import DiscussionForm, GeneralInfoForm
from .models import (Answer, Aspect, AssignedEvaluation, Discussion, Document,
                    EvaluatorOption, FileAttachment, GeneralInfo,
                    Question, QuestionOption, EvaluatorResponse)
from .tables import AspectTable, DocumentTable, EvaluationTable, ScoreTable
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

# def score_all_evaluation(request):
#     return render(request, 'score_dashboard.html')

def score_detail(request):
    return render(request, 'evaluation_score_summary.html')

def show_discussion(request):
    results = Discussion.objects.all()
    return render(request, 'discussion_list.html', {'results': results})

def show_evaluation(request):
    return render(request, 'evaluation_form.html') # TODO: Map date later

def show_evaluator(request):
    return render(request, 'evaluator_form_template.html') # TODO: Map date later

def evaluator_view(request, aspect_id):
    aspect = get_object_or_404(Aspect, id=aspect_id)
    questions = Question.objects.filter(aspect=aspect)
    
    question_with_options = []
    for question in questions:
        options = EvaluatorOption.objects.filter(question=question)
        question_with_options.append({
            'question': question,
            'options': options
        })
    
    context = {
        'aspect': aspect,
        'question_with_options': question_with_options,
    }
    return render(request, 'evaluator_form.html', context)

def evaluator_view_new(request, aspect_id, assigned_user_id):
    #TODO: load evaluator response if already answered
    aspect = get_object_or_404(Aspect, id=aspect_id)
    questions = Question.objects.filter(aspect=aspect)
    answers = Answer.objects.filter(user=assigned_user_id)
    
    question_with_options = []
    for question in questions:
        # Get evaluator options for each question
        options = EvaluatorOption.objects.filter(question=question)
        # Get answers for the subquestions related to the current question
        question_answers = answers.filter(subquestion__question=question)

        question_with_options.append({
            'question': question,
            'options': options,
            'answers': question_answers
        })
    
    context = {
        'aspect': aspect,
        'question_with_options': question_with_options,
        'assigned_user_id': assigned_user_id,
    }

    if request.method == 'POST':
        # Save evaluator responses
        for question in aspect.questions.all():
            evaluator_score = request.POST.get(f'question_{question.id}')
            if evaluator_score:
                EvaluatorResponse.objects.create(
                    question=question,
                    evaluator=request.user,
                    assigned_user_id=assigned_user_id,
                    score=int(evaluator_score)
                )
        
        messages.success(request, "Evaluation submitted successfully!")
        return render(request, 'evaluator_form.html', context) #TODO: fix later
    
    return render(request, 'evaluator_form.html', context)
    
def evaluation_view(request, aspect_id):
    #TODO: load user answer if already answered
    aspect = get_object_or_404(Aspect, pk=aspect_id)
    # file_attachments = FileAttachment.objects.filter(question=aspect)
    
    context = {
        # 'file_attachments': file_attachments,
        # 'evaluation': evaluation,
        'aspect': aspect,
        # 'assigned_user_id': assigned_user_id,
    }
    if request.method == 'POST':
        # Handle the file uploads
        assigned_user = request.user
        
        # Loop through all questions for the specific aspect
        for question in Question.objects.all():
            # Process the file uploads for each question
            file_key = f'document_file_{question.id}'
            if file_key in request.FILES:
                uploaded_file = request.FILES[file_key]
                fs = FileSystemStorage()
                file_path = fs.save(uploaded_file.name, uploaded_file)
                
                # Create a FileAttachment instance
                FileAttachment.objects.create(
                    file=file_path,
                    question=question,
                    uploader=assigned_user
                )

            # Handle subquestion responses
            for subquestion in question.subquestions.all():
                response_key = f'subquestion-{subquestion.id}'
                
                # Handle open text questions
                if subquestion.question_type in  ['text', 'yes_or_no' ]:
                    response_text = request.POST.get(response_key, '')
                    Answer.objects.create(
                        subquestion=subquestion,
                        user=assigned_user,
                        text_answer=response_text
                    )
                
                # Handle one-selection questions (radio buttons)
                elif subquestion.question_type == 'one_selection':
                    selected_option_id = request.POST.get(response_key, '')
                    selected_option = QuestionOption.objects.get(id=selected_option_id)
                    answer = Answer.objects.create(
                        subquestion=subquestion,
                        user=assigned_user,
                    )
                    answer.selected_options.add(selected_option)
                
                # Handle multi-selection questions (checkboxes)
                elif subquestion.question_type == 'multi_selection':
                    selected_option_ids = request.POST.getlist(f'{response_key}-option')
                    answer = Answer.objects.create(
                        subquestion=subquestion,
                        user=assigned_user,
                    )
                    for option_id in selected_option_ids:
                        selected_option = QuestionOption.objects.get(id=option_id)
                        answer.selected_options.add(selected_option)

        # Redirect to a success page or display a success message
        return render(request, 'evaluation_asigned_form.html', context)

    # If it's a GET request, render the form
    return render(request, 'evaluation_asigned_form.html', context)

def create_discussion(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('discussion-show-all')
    else:
        form = DiscussionForm()

    return render(request, 'discussion_form.html', {'form': form})

def general_info_search(request):
    form = GeneralInfoForm()
    results = None
    
    if request.method == 'POST':
        form = GeneralInfoForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            results = GeneralInfo.objects.filter(keyword__icontains=keyword)
    
    return render(request, 'general_info.html', {'form': form, 'results': results})

def pdf_view(request, pk):
    document = get_object_or_404(Document, pk=pk)
    return render(request, 'pdf_viewer.html', {'document': document})

class ScoreListView(SingleTableMixin, FilterView):
    table_class = ScoreTable
    model = AssignedEvaluation
    template_name = "evaluation_list.html"

class EvaluationListView(SingleTableMixin, FilterView):
    #TODO : add condition if evaluator show all
    #TODO : if assigned user only show if the user is in assigned_user
    table_class = EvaluationTable
    model = AssignedEvaluation
    template_name = "evaluation_list.html"

class AspectListView(SingleTableMixin, FilterView):
    #TODO : add condition if asigned user show all
    #TODO : if evaluator only show the evaluator assigned
    table_class = AspectTable
    model = Aspect
    template_name = "aspect_list.html"
    filterset_class = AspectFilter
    # context_object_name = 'aspects'

    # def get_queryset(self):
    #     #TODO: Filter aspects based on the survey's primary key (pk)
    #     # return Aspect.objects.filter(evaluation=self.kwargs['pk'])

    # def get_context_data(self, **kwargs):

    #     context = super().get_context_data(**kwargs)
    #     context['evaluation'] = Evaluation.objects.get(pk=self.kwargs['pk'])
    #     return context


class DocumentListView(SingleTableView):
    model = Document
    table_class = DocumentTable
    template_name = "document_list.html"