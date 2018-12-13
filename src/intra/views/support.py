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
class Support(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'intra/support.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Soporte'
        context['APP'] = 'Support'
        return context
