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
from .models import (Answer, Aspect, AssignedEvaluation, Discussion,
                    EvaluatorOption, FileAttachment, GeneralInfo,
                    Question, QuestionOption, EvaluatorResponse, Document)
from .tables import AspectTable, EvaluationTable, ScoreTable, EvaluatorTable
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'index.html')

def score_detail(request, evaluation_id):
    assigned_evaluation = get_object_or_404(AssignedEvaluation, id=evaluation_id)
    aspects_with_scores = []
    aspects = Aspect.objects.all()

    for aspect in aspects:
        total_score = 0
        questions = Question.objects.filter(aspect=aspect)
        question_with_scores = []

        for question in questions:
            evaluator_responses = EvaluatorResponse.objects.filter(
                question=question, assigned_user=assigned_evaluation.assigned_user
            )

            if evaluator_responses.exists():
                for response in evaluator_responses:
                    total_score += response.calculate_score()

            question_with_scores.append({
                'question': question,
                'evaluator_responses': evaluator_responses,
            })
        aspects_with_scores.append({
            'aspect': aspect,
            'questions_with_scores': question_with_scores,
            'total_score': total_score
        })
    context = {
        'assigned_evaluation': assigned_evaluation,
        'aspects_with_scores': aspects_with_scores
    }

    return render(request, 'evaluation_score_summary.html', context)

def show_discussion(request):
    results = Discussion.objects.all()
    return render(request, 'discussion_list.html', {'results': results})

@login_required 
def evaluator_view(request, assigned_user_id):
    
    evaluator = request.user
    aspect = get_object_or_404(Aspect, evaluator=evaluator)
    questions = Question.objects.filter(aspect=aspect)
    answers = Answer.objects.filter(user=assigned_user_id)

    evaluator_responses = EvaluatorResponse.objects.filter(assigned_user=assigned_user_id)
    
    question_with_options = []
    for question in questions:
        options = EvaluatorOption.objects.filter(question=question)
        question_answers = answers.filter(subquestion__question=question)

        question_responses = evaluator_responses.filter(question=question)

        question_with_options.append({
            'question': question,
            'options': options,
            'answers': question_answers,
            'responses': question_responses
        })
    
    context = {
        'aspect': aspect,
        'question_with_options': question_with_options,
        'assigned_user_id': assigned_user_id,
        'response': {}
    }

    for question in questions:
        question_response = evaluator_responses.filter(question=question).first()  # Get the first response for each question
        if question_response:
            context['response'][f'question{question.id}'] = question_response.score

    if request.method == 'POST':
        for question in aspect.questions.all():
            evaluator_score = request.POST.get(f'question_{question.id}')
            if evaluator_score:
                evaluator_response, created = EvaluatorResponse.objects.get_or_create(
                    question=question,
                    evaluator=request.user,
                    assigned_user_id=assigned_user_id,
                    score=int(evaluator_score)
                )
                evaluator_response.score = int(evaluator_score)
                evaluator_response.save()
        
        messages.success(request, "Evaluation submitted successfully!")
        return render(request, 'evaluator_form.html', context)
    
    return render(request, 'evaluator_form.html', context)
    
@login_required    
def evaluation_view(request, aspect_id):
    aspect = get_object_or_404(Aspect, pk=aspect_id)
    assigned_user = request.user
    
    context = {
        'aspect': aspect,
        'answers': {}
    }
    for question in aspect.questions.all():
        #TODO: also load the uploaded document
        for subquestion in question.subquestions.all():
            answer = Answer.objects.filter(subquestion=subquestion, user=assigned_user).first()
            if answer:
                if subquestion.question_type in ['text', 'yes_or_no']:
                    context['answers'][f'subquestion{subquestion.id}'] = answer.text_answer
                elif subquestion.question_type in ['one_selection', 'multi_selection']:
                    selected_options = answer.selected_options.all()
                    context['answers'][f'subquestion{subquestion.id}'] = [option.id for option in selected_options]
        # document = FileAttachment.objects.filter(question=question, uploader=assigned_user).first()
        # if document:
        #     context['documents'][question.id] = document.file

    if request.method == 'POST':
        for question in Question.objects.all():
            file_key = f'document_file_{question.id}'
            if file_key in request.FILES:
                uploaded_file = request.FILES[file_key]
                fs = FileSystemStorage()
                file_path = fs.save(uploaded_file.name, uploaded_file)
                file_attachment, created = FileAttachment.objects.get_or_create(
                    question=question,
                    uploader=assigned_user,
                )
                file_attachment.file = file_path  # Update the file path
                file_attachment.save()

            for subquestion in question.subquestions.all():
                response_key = f'subquestion-{subquestion.id}'
                
                if subquestion.question_type in  ['text', 'yes_or_no']:
                    response_text = request.POST.get(response_key, '')
                    answer, created = Answer.objects.get_or_create(
                        subquestion=subquestion,
                        user=assigned_user,
                    )
                    answer.text_answer = response_text
                    answer.save()
                
                elif subquestion.question_type in ['multi_selection','one_selection']:
                    selected_option_ids = request.POST.getlist(f'{response_key}-option')
                    answer, created = Answer.objects.get_or_create(
                        subquestion=subquestion,
                        user=assigned_user,
                    )
                    answer.selected_options.clear()
                    for option_id in selected_option_ids:
                        selected_option = QuestionOption.objects.get(id=option_id)
                        answer.selected_options.add(selected_option)
                    answer.save()

        return render(request, 'evaluation_asigned_form.html', context)

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
    template_name = "score_dashboard.html"

class EvaluationListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    #TODO : if assigned user only show if the user is in assigned_user
    table_class = EvaluationTable
    model = AssignedEvaluation
    template_name = "evaluation_list.html"

    def get_queryset(self):
        return AssignedEvaluation.objects.filter(assigned_user=self.request.user)

class EvaluatorListView(SingleTableMixin, FilterView):
    table_class = EvaluatorTable
    model = AssignedEvaluation
    template_name = "evaluator_list.html"

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

