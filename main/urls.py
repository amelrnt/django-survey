from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from .views import (AspectListView, EvaluationListView, EvaluatorListView,
                    ScoreListView, create_discussion, evaluation_view,
                    evaluator_view, general_info_search, index, pdf_view,
                    score_detail, show_discussion)

urlpatterns = [
    path("", index, name="index"),
    path('admin/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("dashboard/", ScoreListView.as_view(), name="score-dashboard"),
    path("dashboard/detail/<int:evaluation_id>", score_detail, name="score-detail"),
    path("discussion/", show_discussion, name="discussion-show-all"),
    path("discussion_create/", create_discussion, name="discussion-create"),
    path("general_info/", general_info_search, name="info-search"),
    path("evaluations/", EvaluationListView.as_view(), name="evaluation-list"),
    path('evaluation/<int:pk>/fill/', AspectListView.as_view(), name='aspect-list'),
    path('evaluation/aspect/<int:aspect_id>', evaluation_view, name='evaluation-form'),
    path('evaluator/', EvaluatorListView.as_view(), name='evaluator-list'),
    path('evaluator/aspect/<int:assigned_user_id>/', evaluator_view, name='evaluator-form'),
    path('view-pdf/<int:pk>/', pdf_view, name='view-pdf'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)