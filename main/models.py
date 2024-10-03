from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('evaluator', 'Evaluator'),
        ('assignee', 'Assignee'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username

class Document(models.Model):
    name = models.CharField(max_length=255)
    document_file = models.FileField(upload_to ='uploads') 

    def __str__(self):
        return self.name

class Discussion(models.Model):
    QUESTION_CHOICES = {
        'Q': "Pertanyaan",
        'S' : "Saran",
    }

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    question_type = models.CharField(
        max_length=1,
        choices=QUESTION_CHOICES,
    )
    assigned_user = models.ForeignKey(User, related_name='assigned_question', on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.question} for {self.assigned_user}"


class GeneralInfo(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    keyword = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Evaluation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('aspect-list', kwargs={'pk': self.pk})

class AssignedEvaluation(models.Model):
    SCORE_CATEGORY = (
        ("A", "Pelayanan Prima"),
        ("A-", "Sangat Baik"),
        ("B", "Baik"),
        ("B-", "Baik(Dengan Catatan)"),
        ("C", "Cukup"),
        ("C-", "Cukup(Dengan Catatan)"),
        ("D", "Buruk"),
        ("E", "Sangat Buruk"),
        ("F", "Gagal"),
    )
    date_start = models.DateField()
    date_end = models.DateField()
    date_deadline = models.DateField()
    assigned_user = models.ForeignKey(User, related_name='assigned_evaluations', on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, related_name='evaluation', on_delete=models.CASCADE)

    score = models.IntegerField(default=0)
    score_category = models.CharField(max_length=5, choices=SCORE_CATEGORY, default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.evaluation.name} {self.assigned_user}"

    def calculate_progress(self):
        total_questions = Question.objects.filter(aspect__evaluation=self).count()
        answered_questions = Answer.objects.filter(subquestion__question__aspect__evaluation=self, user=self.assigned_user).count()
        if total_questions == 0:
            return 0
        return (answered_questions / total_questions) * 100

    def calculate_final_score(self):
        evaluator_responses = self.evaluator_responses.all()  # Use related_name to access EvaluatorResponse
        if evaluator_responses.exists():
            total_score = sum([response.score for response in evaluator_responses])
            return total_score / evaluator_responses.count()  # Average score from all evaluators
        return 0

    def calculate_grade(self):
        score = self.calculate_final_score()
        # TODO: Convert the score to a grade (customize logic)
        if score >= 90:
            return "A"
        elif score >= 80:
            return "A-"
        elif score >= 70:
            return "B"
        # Continue with grading logic...

    def get_absolute_url(self):
        return reverse('aspect-list', kwargs={'pk': self.pk})
    
    def get_evaluator_url(self):
        return reverse('evaluator-form', kwargs={'assigned_user_id': self.assigned_user_id})
    
    def get_scoring_detail_url(self):
        return reverse('score-detail', kwargs={'evaluation_id': self.id})

class Aspect(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    evaluator = models.ForeignKey(User, related_name='aspect_evaluator', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def count_subquestion(self):
        return 0
    
    def count_answer(self):
        return 0

    def get_absolute_url(self):
        return reverse('evaluation-form', kwargs={'aspect_id': self.pk})

class Question(models.Model):
    aspect = models.ForeignKey(Aspect, related_name='questions', on_delete=models.CASCADE)
    name = models.TextField()
    point_weight = models.FloatField(help_text='The percentage weight of this question within the aspect')

    def __str__(self):
        return self.name

# Possible answer options for questions
class QuestionOption(models.Model):
    subquestion = models.ForeignKey('SubQuestion', related_name='options', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text

# Sub-question model to handle different answer types
class SubQuestion(models.Model):
    QUESTION_TYPES = (
        ('text', 'Jawaban Terbuka'),
        ('yes_or_no', 'Ya/Tidak'),
        ('one_selection', 'Pilih Salah 1'),
        ('multi_selection', 'Pilih lebih dari 1'),
    )
    question = models.ForeignKey('Question', related_name='subquestions', on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    def __str__(self):
        return self.question_text

# Answer model for respondents
class Answer(models.Model):
    subquestion = models.ForeignKey(SubQuestion, related_name='answers', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='answers', on_delete=models.CASCADE)
    text_answer = models.TextField(blank=True, null=True)  # For open text type
    selected_options = models.ManyToManyField(QuestionOption, blank=True)  # For one/multi-selection type

    def __str__(self):
        return f"Answer by {self.user} for {self.subquestion}"

# table to store option for evaluator choices
class EvaluatorOption(models.Model):
    question = models.ForeignKey(Question, related_name='evaluation_questions', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(0, 6)])

    def calculate_score(self):
        """Calculate the final score based on the evaluator's selection."""
        return round((self.score / 5) * self.question.point_weight, 2)

    def __str__(self):
        return f"Option {self.score} for {self.question}"

# Evaluator's response to a question
class EvaluatorResponse(models.Model):
    question = models.ForeignKey(Question, related_name='evaluator_responses', on_delete=models.CASCADE)
    evaluator = models.ForeignKey(User, related_name='evaluator', on_delete=models.CASCADE)
    assigned_user = models.ForeignKey(User, related_name='assigned_responses', on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(0, 6)])  # 1-5 scale

    def calculate_score(self):
        """Calculate the final score based on the evaluator's selection."""
        return round((self.score / 5) * self.question.point_weight, 2)

    def __str__(self):
        return f"Response by {self.evaluator} for {self.question}"

class FileAttachment(models.Model):
    question = models.ForeignKey(Question, related_name='attachments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
    description = models.TextField(blank=True, null=True)
    uploader = models.ForeignKey(User, related_name='assigned_user', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.file.name} uploaded by {self.uploader} on {self.question.name}"

