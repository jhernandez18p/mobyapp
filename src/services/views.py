from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse

from .models import Service

# Create your views here.
class Home(ListView):
    # model =
    # context_object_name = 'boards'
    model = Service
    template_name = 'app/services.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        
        context['has_newsletter'] = True
        context['SITE_URL'] = 'Services'
        # context['services'] = queryset
        context['url'] = reverse('services:home')

        
        return context


class ServiceDetail(DetailView):

    model = Service
    template_name = 'app/detail/service_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context