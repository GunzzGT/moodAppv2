from django.urls import path

from .views import (
    LoginView,
    RefreshView,
)

urlpatterns = [
    path("user/signin/", LoginView.as_view(), name="LoginTokenCreate"),
    path("user/refresh/", RefreshView.as_view(), name="LoginTokenRefresh"),
]
