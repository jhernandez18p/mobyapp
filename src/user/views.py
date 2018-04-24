import urllib
import json

from django.conf import settings
from django.contrib import auth, messages
from django.contrib.messages import get_messages
from django.contrib.auth import login, authenticate,REDIRECT_FIELD_NAME, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse 
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View, ListView, FormView, TemplateView, RedirectView

from .models import Newsletter
from .auth import account_activation_token
from .forms import SignUpForm,NewsletterForm
from src.utils.libs import newsletter_email

from src.user.tokens import account_activation_token

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.profile.email_confirmed = True
            user.profile.status = 'ACTIVE'
            user.save()
            login(request, user)
            return redirect('intra')
        else:
            # invalid link
            return render(request, 'auth/invalid.html')


class SignUp(FormView):
    """
    Custom user creation
    """


def modal_cookie(request):
    username = request.GET.get('username', None)

    return JsonResponse(username)

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
        # Method Get
        return render(request, "auth/form.html", context)
    
    elif request.method == "POST":
        # Method Post
        username = request.POST['username']
        password = request.POST['password']

        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''
        # print(result)
        if result['success']:
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
                    return render(request, "auth/form.html", { "warning": "Su Cuenta no esta activa" })
            else:
                #User is None
                messages.add_message(request, messages.INFO, 'Ha ocurrido un error con su nombre de usuario o contraseña, por favor vuelva a intentar.')
                return HttpResponseRedirect('/auth/error')

        else:
            # Error reCAPTCHA
            messages.add_message(request, messages.INFO, 'Ha ocurrido un error con la validación de sus datos, por favor vuelva a intentar.')
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
            
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            useremail = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            
            if result['success']:
                if User.objects.get(email=useremail):
                    messages.add_message(request, messages.INFO, 'Ups... Ha ocurrido un error el usuario que introdujo ya existe.')
                    return HttpResponseRedirect('/auth/error')
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
                        # User is not active
                        messages.add_message(request, messages.INFO, 'Ups... Parece que no ha activado su cuenta aún.')
                        return HttpResponseRedirect('/auth/error')
                else:
                    messages.add_message(request, messages.INFO, 'No ha sido posible validar el nombre de usuario, por favor vuelva a intentarlo.')
                    return HttpResponseRedirect('/auth/error')
        else:
            messages.add_message(request, messages.INFO, 'Ups... Ha ocurrido un error, los datos puede que sean invalidos.')
            return HttpResponseRedirect('/auth/error')
    else:
        return render(request, "auth/form.html", context)

def newsletter(request):
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

def page_not_found_view(request):
    # my custom page not found view
    template = 'auth/page_not_found_view.html'
    context = {}
    context['error_code'] = "404"
    return render(request,template,context)

def error_view(request):
    # my custom error view
    template = 'auth/error_view.html'
    context = {}
    context['error_code'] = "500"
    return render(request,template,context)

def permission_denied_view(request):
    # my custom permission denied view
    template = 'auth/permission_denied_view.html'
    context = {}
    context['error_code'] = "403"
    return render(request,template,context)

def bad_request_view(request):
    # my custom bad request view
    template = 'auth/bad_request_view.html'
    context = {}
    context['error_code'] = "400"
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
        return render(request, 'auth/error.html')