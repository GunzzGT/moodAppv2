from django.urls import path

from .views import (
    ViewSelf,
)

urlpatterns = [
    path('user/account/manage/', ViewSelf.as_view(), name='ViewSelf'),
]
