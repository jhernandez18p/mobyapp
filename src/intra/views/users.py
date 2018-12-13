from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_text, force_bytes
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from src.user.tokens import account_activation_token
from src.blog.models import Comment



@method_decorator(login_required, name='dispatch')
class Profile(ListView):
    model = User
    template_name = 'intra/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        user = self.request.user
        comments = Comment.objects.all()
        if comments.exists():
            context['comments'] = comments.filter(author=user)
        context['menu'] = 'profile'
        context['SITE_URL'] = 'Perfil de %s' % (self.request.user.username)
        context['APP'] = 'Profile'
        return context


@method_decorator(login_required, name='dispatch')
class Users(ListView):
    model = User
    template_name = 'intra/users.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'users'
        context['SITE_URL'] = 'Intra'
        context['APP'] = 'Users'
        return context



@method_decorator(login_required, name='dispatch')
class UserCreate(CreateView):
    model = User
    fields = ['first_name','last_name','email','username','password']
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UserUpdate(UpdateView):
    model = User
    fields = ['first_name','last_name','email','username',]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return '/intra/usuarios'


@method_decorator(login_required, name='dispatch')
class UserDelete(DeleteView):
    model = User
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


