from django.contrib.sessions.backends.db import SessionStore
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView

from src.base.forms import ContactForm
from src.base.models import Position, Carousel, CarouselImage, Site
from src.blog.models import Comment, Post
# from src.utils.libs import contact_email
from src.ventas.models import Department


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
    queryset = ''
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        home_header_carousel = Carousel.objects.filter(Q(page_id=1) & Q(position_id=1))
        if home_header_carousel.exists():
            context['home_header_carousel'] = True
            
            home_header_carousel_images = CarouselImage.objects.filter(Carousel_id=1)
            if home_header_carousel_images.exists():
                context['home_header_carousel_images'] = home_header_carousel_images

        departments = Department.objects.all()
        if departments.exists():
            context['departments'] = departments[:4]

        posts = Post.objects.filter(draft=False)
        if posts.exists():
            context['blog_post'] = posts[:3]

        context['has_newsletter'] = True
        context['SITE_URL'] = 'Inicio'
        context['url'] = reverse('front:home')
        context['url_nav'] = 'inicio'
        
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
        context['url_nav'] = '¿Quienes somos?'
        return context


class Contact(ListView):
    form_class = ContactForm
    queryset = ''
    template_name = 'app/contact.html'

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
        context['url_nav'] = 'contacto'
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
        context['url_nav'] = 'buscar'
        return context


class ContactThanks(View):
    template_name = 'app/base/thanks.html'


    def get(self, request, *args, **kwargs):
        context = {}
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name, context)


class ContactError(View):
    template_name = 'app/base/error.html'


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