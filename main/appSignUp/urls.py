from django.urls import path

from .views import (
    CreateUserView,
)

urlpatterns = [
    path('user/signup/', CreateUserView.as_view(), name='CreateUser'),
]
