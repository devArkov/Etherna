from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post


# Create your views here.
class BlogList(ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context


class BlogDetail(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

