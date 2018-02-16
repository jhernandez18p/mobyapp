from django.contrib.sessions.backends.db import SessionStore
from django.http import (HttpResponse, HttpResponseRedirect, JsonResponse)
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import render

from src.base.forms import (ContactForm)
from src.base.models import *
from src.blog.models import (Comment, Post)
from src.ventas.models import (Department)


class AjaxableSessionResponseMixin:
    """
        Mixin to add AJAX support to a form.
        Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class Home(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        home_header_carousel = Carousel.objects.all().filter(page_id=1).filter(position_id=1)
        if home_header_carousel.exists():
            context['home_header_carousel'] = True
            
            home_header_carousel_images = CarouselImage.objects.all().filter(Carousel_id=1)
            if home_header_carousel_images.exists():
                context['home_header_carousel_images'] = home_header_carousel_images

        info_site = Site.objects.all()
        if info_site.exists():
            context['site_info'] = info_site[0]
            # print(context['info_site'].services_img.url)

        departments = Department.objects.all()
        if len(departments) >= 1:
            context['departments'] = departments

        posts = Post.objects.all()
        if posts.exists():
            context['blog_post'] = posts[:3]
            
        
        context['has_newsletter'] = True
        context['SITE_URL'] = 'Inicio'
        context['url'] = reverse('front:home')
        context['blog_post_test'] = [
            {
                'title':'Esto es un post',
                'sub_title':'New post 01',
                'text':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe ipsa nam facere fugiat maiores iste, placeat ratione consequuntur. Laboriosam in eos non dolores sit enim quaerat saepe exercitationem possimus ratione?',
                'background':'https://static.pexels.com/photos/261579/pexels-photo-261579.jpeg',
                'img':'/static/base/img/moby-background-01.png',
                'time_stamp':'01/01/2018',
                'slug':'new_post_1',
            },
            {
                'title':'Esto es un post',
                'sub_title':'New post 01',
                'text':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe ipsa nam facere fugiat maiores iste, placeat ratione consequuntur. Laboriosam in eos non dolores sit enim quaerat saepe exercitationem possimus ratione?',
                'background':'https://static.pexels.com/photos/261579/pexels-photo-261579.jpeg',
                'img':'/static/base/img/moby-background-01.png',
                'time_stamp':'01/01/2018',
                'slug':'new_post_2',
            },
            {
                'title':'Esto es un post',
                'sub_title':'New post 01',
                'text':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe ipsa nam facere fugiat maiores iste, placeat ratione consequuntur. Laboriosam in eos non dolores sit enim quaerat saepe exercitationem possimus ratione?',
                'background':'https://static.pexels.com/photos/261579/pexels-photo-261579.jpeg',
                'img':'/static/base/img/moby-background-01.png',
                'time_stamp':'01/01/2018',
                'slug':'new_post_3',
            }
        ]
        
        return context


class About(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/about.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Moby'
        return context


class Services(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/services.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Nuestros servicios'
        context['has_newsletter'] = True
        return context


class Contact(ListView):
    # model =
    # context_object_name = 'boards'
    form_class = ContactForm
    queryset = ''
    template_name = 'app/contact.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/contacto/gracias')
        else:
            return HttpResponseRedirect('/contacto/error')
        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        form = self.form_class
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Contactanos'
        context['form'] = form
        return context


class Search(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/search.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Buscar'
        return context


class ContactThanks(View):
    template_name = 'app/contact_thanks.html'


    def get(self, request, *args, **kwargs):
        context = {}
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name, context)


class ContactError(View):
    template_name = 'app/contact_error.html'


    def get(self, request, *args, **kwargs):
        context = {}
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name, context)


def session(request):
    cookie_modal = request.GET.get('cookie_modal', None)
    cookie = SessionStore()
    data = {}

    if str(cookie_modal) == 'true':
        cookie['cookie_modal'] = True
        data['cookie_is_set'] = True
        print('ok')
    else:
        cookie['cookie_modal'] = False
        data['cookie_is_set'] = False


    if data['cookie_is_set']:
        data['error_message'] = 'Aun no se han creado la cookie.'
    else:
        data['success_message'] = 'En hora buena!.'

    cookie.create()
    return JsonResponse(data)