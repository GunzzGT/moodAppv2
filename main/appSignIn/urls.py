from django.urls import path

from .views import (
    LoginView,
    RefreshView,
)

urlpatterns = [
    path("signin/", LoginView.as_view(), name="LoginTokenCreate"),
    path("refresh/", RefreshView.as_view(), name="LoginTokenRefresh"),
]
