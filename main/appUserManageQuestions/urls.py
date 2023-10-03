from django.urls import path

from .views import (
    CreateUserQuestionView,
)

urlpatterns = [

    path('user/question/init/', CreateUserQuestionView.as_view(), name='CreateQuestionTemplate'),
]
