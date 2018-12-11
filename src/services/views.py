from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView


from src.services.models import Service, ServiceImage
from src.services.forms import ServiceForm
from src.base.models import Position, Carousel, CarouselImage, Site
from src.utils.libs import contact_email

# Create your views here.
class Home(ListView):
    model = Service
    template_name = 'app/services.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        service_list = self.model.objects.all()
        if service_list.exists():
            context = super().get_context_data(object_list=service_list.filter(featured=False),service_list=service_list.filter(featured=True),**kwargs)

        service_header_carousel = Carousel.objects.filter(Q(page__name='servicios') & Q(position__name='header'))
        if service_header_carousel.exists():
            context['service_header_carousel'] = True
            
            service_header_carousel_images = CarouselImage.objects.filter(Carousel_id=service_header_carousel[0])
            if service_header_carousel_images.exists():
                context['service_header_carousel_images'] = service_header_carousel_images

        context['has_newsletter'] = True
        context['SITE_URL'] = 'Servicios'
        context['url'] = reverse('services:home')
        context['url_nav'] = 'servicios'

        return context


class ServiceDetail(DetailView):

    model = Service
    form_class = ServiceForm
    paginate_by = 6
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
        context['form'] = form
        images = ServiceImage.objects.filter(Service_id=context['object'].id)
        if images.exists():
            context['has_images'] = True
            context['images'] = images

        obj = super().get_object()
        services = self.model.objects.exclude(slug=obj.slug).order_by('?')[:3]
        if services.exists():
            context['object_list'] = services

        context['url_nav'] = 'servicios'
        return context


class ServiceThanks(ListView):
    model = Service
    template_name = 'app/base/thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_newsletter'] = True
        context['SITE_URL'] = 'Servicios'
        context['url'] = reverse('services:home')
        context['url_nav'] = 'servicios'

        return context


class ServiceError(ListView):
    model = Service
    template_name = 'app/base/error.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_newsletter'] = True
        context['SITE_URL'] = 'Servicios'
        context['url_nav'] = 'servicios'
        context['url'] = reverse('services:home')

        return context