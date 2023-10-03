from django.urls import path

from .views import (
    CreateQuestionView,
    FillQuestionView,
    CreateUserQuestionView,
)

urlpatterns = [
    path('adm/question/create/', CreateQuestionView.as_view(), name='CreateQuestionTemplate'),
    path('adm/question/fill/<str:pk>/', FillQuestionView.as_view(), name='FillQuestionTemplate'),
    path('adm/question/user/create/<str:pk>/', CreateUserQuestionView.as_view(), name='CreateUserQuestionSet'),
]
