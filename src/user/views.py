from django.conf import settings
from django.contrib import auth
from django.contrib.auth import login, authenticate,REDIRECT_FIELD_NAME, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect,JsonResponse 
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, FormView, TemplateView, RedirectView
from urllib.parse import urlparse

from .models import Newsletter
from .auth import account_activation_token
from .forms import SignUpForm,NewsletterForm
from src.utils.libs import newsletter_email

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

def error(request):
    context = {}
    template = 'auth/error.html'
    context['SITE_URL'] = 'Error'
    return render(request, template, context)

def thanks(request):
    return HttpResponseRedirect('/')

def custom_login(request):
    context = {}
    context['SITE_URL'] = 'Iniciar Sesión'
    context['form_name'] = 'Inicio de Sesión'
    context['form_button'] = 'Inicar Sesión'
    context['form'] = AuthenticationForm

    if request.method == "GET":
        return render(request, "auth/form.html", context)
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                _next = "/auth/gracias"
                if "next" in request.GET:
                    _next = request.GET["next"]
                if _next == None or _next == "":
                    _next = "/"
                return HttpResponseRedirect(_next)
            else:
                return render(request, "auth/form.html", { "warning": "Your account is disabled" })
        else:
            return HttpResponseRedirect('/auth/error')

def custom_logout(request):
    auth.logout(request)
    _next = "/"
    if "next" in request.GET:
        _next = request.GET["next"]
    if _next == None or _next == "":
        _next = "/"
    return HttpResponseRedirect(_next)

def custom_register(request):
    form = SignUpForm(request.POST)
    context = {}
    context['form'] = form
    context['SITE_URL'] = 'Registrarse'
    context['form_name'] = 'Registro de usuario'
    context['form_button'] = 'Registrarse'

    if request.method == "POST":
        if form.is_valid():
            useremail = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            try:
                User.objects.get(email=useremail)
                print('User exists')
                return HttpResponseRedirect('/auth/error')
            except User.DoesNotExist:
                form.save()
                user = auth.authenticate(username = useremail, password = password)
                if user is not None:
                    if user.is_active:
                        auth.login(request, user)
                        _next = "/auth/gracias"
                        if "next" in request.GET:
                            _next = request.GET["next"]
                        if _next == None or _next == "":
                            _next = "/auth/gracias"
                        return HttpResponseRedirect(_next)
                    else:
                        return HttpResponseRedirect('/auth/error')
                else:
                    if "next" in request.GET:
                        _next = request.GET["next"]
                    if _next == None or _next == "":
                        _next = "/auth/error"
                    print('Error user is None')
                    return HttpResponseRedirect(_next)
        else:
            print('Form invalid')
            return HttpResponseRedirect('/auth/error')

    return render(request, "auth/form.html", context)


def Newsletter(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/contacto/error')
    else:

        form_name = request.GET.get('Nombre')
        form_email = request.GET.get('Correo')
        print(request.GET.get('Nombre'))
        print('\n\n')
        print(request.GET.get('Correo'))
        
        a = newsletter_email(
            form_name,
            form_email,
            # form_subject,
            # form_message,
            # form_service,
        )

        if a:
            newsletter = Newsletter.objects.filter(Q(name=form_name) | Q(email=form_email))
            if newsletter:
                Newsletter(name=form_name,email=form_email)




