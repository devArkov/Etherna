from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Home'
        return context


class About(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'About'
        return context


class Contact(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Contact'
        return context


def handle_not_found(request, exception):
    return render(request, '404.html')
