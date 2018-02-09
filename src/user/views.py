from urllib.parse import urlparse
from django.conf import settings

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .auth import account_activation_token

# Create your views here.
from django.views.generic import ListView, FormView, TemplateView, RedirectView
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

# Authentication imports
from django.contrib.auth import REDIRECT_FIELD_NAME, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import JsonResponse

from django.urls import reverse_lazy
from .forms import SignUpForm


class Login(FormView):

    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'auth/form.html'
    success_url =  reverse_lazy("intra:home")

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        url_next = request.GET.get('next')
        if request.user.is_authenticated:
            if url_next:
                return HttpResponseRedirect(url_next)
            else:
                return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        if self.success_url:
            redirect_to = self.request.GET.get('next')
        else:
            redirect_to = self.success_url
        return redirect_to

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

    def set_test_cookie(self):
        self.request.session.set_test_cookie()

    def check_and_delete_test_cookie(self):
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
            return True
        return False

    def get(self, request, *args, **kwargs):
        self.set_test_cookie()
        return super(Login, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.check_and_delete_test_cookie()
            return self.form_valid(form)
        else:
            self.set_test_cookie()
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Iniciar Sesión'
        context['form_name'] = 'Inicio de Sesión'
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

def Register(request):
    template = 'auth/form.html'
    context = {}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm
        # return render(request, 'signup.html', {'form': form})
        context['form'] = form
        context['SITE_URL'] = 'Registrarse'
        context['form_name'] = 'Registro de usuario'
        context['form_button'] = 'Registrarse'
        return render(request,template,context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


def modal_cookie(request):
    username = request.GET.get('username', None)

    return JsonResponse(data)