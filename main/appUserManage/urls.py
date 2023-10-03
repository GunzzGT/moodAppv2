from django.urls import path

from .views import (
    ViewSelf,
)

urlpatterns = [
    path('user/manage/', ViewSelf.as_view(), name='ViewSelf'),
]
