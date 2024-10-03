import django_tables2 as tables
from django.utils.html import format_html
from .models import Evaluation, Aspect, AssignedEvaluation

class EvaluationTable(tables.Table):
    progress = tables.Column()

    # Custom column for the button
    fill_survey = tables.Column(empty_values=(), verbose_name="Action")
    evaluation_info = tables.Column(empty_values=(), verbose_name="Evaluation Info")

    def render_fill_survey(self, record):
        return format_html(
            '<a href="{}" class="btn btn-primary">See Details</a>',
            record.get_absolute_url()
        )
    
    def render_evaluation_info(self, record):
        return str(record)
    
    def render_progress(self, record):
        progress_value = record.calculate_progress()
        return f"{progress_value:.2f}%"

    class Meta:
        model = AssignedEvaluation
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ("evaluation_info", "date_start", "date_end", "date_deadline" ,"progress")

class EvaluatorTable(tables.Table):
    progress = tables.Column()

    # Custom column for the button
    fill_survey = tables.Column(empty_values=(), verbose_name="Action")
    evaluator_info = tables.Column(empty_values=(), verbose_name="Evaluation Info")

    def render_fill_survey(self, record):
        return format_html(
            '<a href="{}" class="btn btn-primary">See Details</a>',
            record.get_evaluator_url()
        )
    
    def render_evaluator_info(self, record):
        return str(record)
    
    class Meta:
        model = AssignedEvaluation
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ("evaluator_info", "date_start", "date_end", "date_deadline" ,"progress")


class ScoreTable(tables.Table):
    # Custom column for the button
    see_details = tables.Column(empty_values=(), verbose_name="Action")
    score_info = tables.Column(empty_values=(), verbose_name="Evaluation Info")

    def render_see_details(self, record):
        return format_html(
            '<a href="{}" class="btn btn-primary">See Details</a>',
            record.get_scoring_detail_url()
        )
    
    def render_score_info(self, record):
        return str(record)

    class Meta:
        model = AssignedEvaluation
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ("score_info", "score", "score_category")


class AspectTable(tables.Table):
    # Define columns
    name = tables.Column(linkify=True)
    question_count = tables.Column()
    answer_count = tables.Column()
    
    # Custom column for the button
    fill_aspect = tables.Column(empty_values=(), verbose_name="Action")

    def render_fill_aspect(self, record):
        return format_html(
            '<a href="{}" class="btn btn-primary">Fill Evaluation</a>',
            record.get_absolute_url()
        )

    class Meta:
        model = Aspect
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ("name", "question_count", "answer_count", "fill_aspect")
