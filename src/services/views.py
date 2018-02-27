from django.core.mail import send_mail,EmailMultiAlternatives
from django.http import (HttpResponse, HttpResponseRedirect, JsonResponse)
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import (Service, ServiceImage)
from .forms import ServiceForm

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
            form_service = form.cleaned_data.get('service')

            subject, from_email, to = 'Solicitud de servicios %s | mensaje enviado' %(form_service), 'info@moby-group.com', form_email
            text_content = 'Su mensaje ha sido enviado correctamente.'
            html_content = '<p>Su mensaje ha sido emviado correctamente.</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return HttpResponseRedirect('/servicios')
        else:
            return HttpResponseRedirect('/servicios')
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