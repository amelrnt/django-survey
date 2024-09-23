import django_tables2 as tables
from django.utils.html import format_html
from .models import Evaluation, Aspect, Document, AssignedEvaluation

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

    class Meta:
        model = AssignedEvaluation
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ("evaluation_info", "date_start", "date_end", "date_deadline" ,"progress")

class ScoreTable(tables.Table):
    # Custom column for the button
    see_details = tables.Column(empty_values=(), verbose_name="Action")
    evaluation_info = tables.Column(empty_values=(), verbose_name="Evaluation Info")

    def render_see_details(self, record):
        return format_html(
            '<a href="{}" class="btn btn-primary">See Details</a>',
            record.get_scoring_detail_url()
        )
    
    def render_evaluation_info(self, record):
        return str(record)

    class Meta:
        model = AssignedEvaluation
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ("evaluation_info", "score", "score_category")


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


class DocumentTable(tables.Table):
    view_document = tables.TemplateColumn(
        # <a href="{{ document.document_file.url }}" target="_blank">{{ document.name }}</a>
        """<a href="http://localhost:8000/uploads/SDN202400076.pdf" target="_blank" class="btn btn-sm btn-primary">View PDF</a>""", #TODO: chang to document link later
        verbose_name='View'
    )

    class Meta:
        model = Document
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ("name",)

        