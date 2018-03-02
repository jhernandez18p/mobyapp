from django.http import (HttpResponseRedirect)
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import (Service, ServiceImage)
from .forms import ServiceForm
from src.utils.libs import contact_email

# Create your views here.
class Home(ListView):
    model = Service
    paginate_by = 6
    template_name = 'app/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_newsletter'] = True
        context['SITE_URL'] = 'Services'
        context['url'] = reverse('services:home')
        return context


class ServiceDetail(DetailView):

    model = Service
    form_class = ServiceForm
    template_name = 'app/detail/service_detail.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form_name = form.cleaned_data.get('name')
            form_email = form.cleaned_data.get('email')
            form_subject = form.cleaned_data.get('subject')
            form_message = form.cleaned_data.get('message')
            form_service = request.GET.get('name')
            
            contact_email(
                (form_name,
                form_email,
                form_subject,
                form_message,
                form_service,)
            )

            return HttpResponseRedirect('/servicios/gracias')
        else:
            return HttpResponseRedirect('/servicios/error')
        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class
        images = ServiceImage.objects.all().filter(Service_id=context['object'].id)
        if images.exists():
            context['has_images'] = True
            context['images'] = images
        context['form'] = form
        return context


class ServiceThanks(ListView):
    model = Service
    template_name = 'app/base/thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_newsletter'] = True
        context['SITE_URL'] = 'Services'
        context['url'] = reverse('services:home')

        return context


class ServiceError(ListView):
    model = Service
    template_name = 'app/base/error.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_newsletter'] = True
        context['SITE_URL'] = 'Services'
        context['url'] = reverse('services:home')

        return context