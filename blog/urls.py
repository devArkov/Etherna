from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog'),
    path('post/<str:slug>', views.BlogDetail.as_view(), name='post'),
]
