from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

class Home(ListView):

    # context_object_name = 'book_list'
    # queryset = Book.objects.filter(publisher__name='ACME Publishing')
    queryset = ''
    template_name = 'frontend/apps/home.html'
    