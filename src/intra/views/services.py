from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_text, force_bytes
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from src.user.tokens import account_activation_token
from src.blog.models import Post, Comment
from src.services.models import *
from src.ventas.models import *


@method_decorator(login_required, name='dispatch')
class Services(ListView):
    model = Service
    template_name = 'intra/services.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        images = ServiceImage.objects.all()
        if images.exists():
            context['images'] = images

        context['menu'] = 'services'
        context['SITE_URL'] = 'services'
        context['APP'] = 'Servicios'
        return context


@method_decorator(login_required, name='dispatch')
class ServiceCreate(CreateView):
    """
    """
    model = Service
    fields = [
        'name',
        'title',
        'description',
        'content',
        'slug',
        'image',
        'featured',
        'position',
        'background',
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ServiceUpdate(UpdateView):
    """
    """
    model = Service
    fields = [
        'name',
        'title',
        'description',
        'content',
        'slug',
        'image',
        'featured',
        'position',
        'background',
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ServiceDelete(DeleteView):
    """
    """
    model = Service
    fields = [
        'name',
        'title',
        'description',
        'content',
        'slug',
        'image',
        'featured',
        'position',
        'background',
    ]
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ServiceIMGCreate(CreateView):
    """
    """
    model = ServiceImage
    fields = [
        'Service',
        'image',
        'name',
        'text',
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ServiceIMGUpdate(UpdateView):
    """
    """
    model = ServiceImage
    fields = [
        'Service',
        'image',
        'name',
        'text',
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ServiceIMGDelete(DeleteView):
    """
    """
    model = ServiceImage
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
