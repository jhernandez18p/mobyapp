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
from src.gallery.models import *



@method_decorator(login_required, name='dispatch')
class Medias(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'intra/medias.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Multimedia'
        context['APP'] = 'Medias'
        return context


@method_decorator(login_required, name='dispatch')
class MediaCreate(CreateView):
    """
    """
    # model = ''
    fields = ['']
    queryset = ''
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class MediaUpdate(UpdateView):
    """
    """
    # model = ''
    fields = ['']
    queryset = ''
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class MediaDelete(DeleteView):
    """
    """
    # model = ''
    fields = ['']
    queryset = ''
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

