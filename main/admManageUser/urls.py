from django.urls import path

from .views import (
    ViewAll,
    ViewOne,
    ViewSelf,
)

urlpatterns = [
    path('adm/user/view/all/', ViewAll.as_view(), name='ViewAll'),
    path('adm/user/view/one/<str:pk>/', ViewOne.as_view(), name='ViewOnePk'),
    path('adm/user/view/self/', ViewSelf.as_view(), name='ViewOneAuth'),
]
