from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, FormView, TemplateView, RedirectView
from django.http import HttpResponseRedirect

# Authentication imports
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.urls import reverse_lazy

class Login(FormView):

    form_class = AuthenticationForm
    template_name = 'auth/form.html'
    success_url =  reverse_lazy("intra:home")


    def dispatch(self, request, *args, **kwargs):
        url = self.get('next')
        print(self.get('url'))
        if request.user.is_authenticated:
            if url != '':
                success_url = url
                return HttpResponseRedirect(self.get_success_url())
            else:
                success_url =  reverse_lazy("intra:home")
                return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Iniciar Sesión'
        context['form_name'] = 'Formulario de Inicio de Sesión'
        context['form_button'] = 'Inicar Sesión'
        return context


class Logout(RedirectView):

    pattern_name = 'front:home'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Salir'
        return context


class Register(FormView):

    form_class = UserCreationForm
    template_name = 'auth/form.html'
    success_url =  reverse_lazy("intra:home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Register, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        Register(self.request, form.get_user())
        return super(Register, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Registrarse'
        context['form_name'] = 'Formulario de Registro'
        context['form_button'] = 'Registrarse'
        return context