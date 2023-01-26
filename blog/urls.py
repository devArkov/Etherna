from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog'),
    # Blog filters
    path('category/<str:slug>', views.CategoryListView.as_view(), name='category'),
    path('post/<str:slug>', views.PostDetailView.as_view(), name='post'),
]
