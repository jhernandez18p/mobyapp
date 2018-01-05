from django.shortcuts import render
from django.views.generic import ListView

class Home(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/home.html'


class About(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/about.html'


class Services(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/services.html'


class Products(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/products.html'


class Contact(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/contact.html'


class Blog(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/blog.html'

class Search(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/search.html'
