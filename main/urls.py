from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from .views import (AspectListView, DocumentListView, EvaluationListView,
                    ScoreListView, create_discussion, evaluation_view,
                    evaluator_view, general_info_search, index, pdf_view,
                    score_detail, show_discussion, show_evaluator, evaluator_view_new)

urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", ScoreListView.as_view(), name="score-dashboard"),
    path("dashboard/detail/", score_detail, name="score_detail"),
    path("discussion/", show_discussion, name="discussion-show-all"),
    path("discussion_create/", create_discussion, name="discussion-create"),
    path("general_info/", general_info_search, name="info-search"),
    path("evaluations/", EvaluationListView.as_view(), name="evaluation-list"),
    path('evaluation/<int:pk>/fill/', AspectListView.as_view(), name='aspect-list'), #TODO: fix later
    path('aspect/', AspectListView.as_view(), name='aspect-list'),
    path('evaluation/aspect/<int:aspect_id>', evaluation_view, name='evaluation-form'),
    path('evaluator/', show_evaluator, name='evaluator-form-template'),
    # path('evaluator/aspect/<int:aspect_id>', evaluator_view, name='evaluator-form'),
    path('evaluator/aspect/<int:aspect_id>/<int:assigned_user_id>/', evaluator_view_new, name='evaluator-form'),
    # path('evaluator/aspect/<int:aspect_id>/<int:asigned_user_id>/', evaluator_view, name='evaluator-form'),
    path('documents/', DocumentListView.as_view(), name='document-list'),
    path('view-pdf/<int:pk>/', pdf_view, name='view-pdf'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)