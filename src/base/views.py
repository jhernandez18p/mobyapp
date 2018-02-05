from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse

from src.blog.models import (Comment, Post)
from src.ventas.models import (Department)

class Home(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        departments = Department.objects.all()
        if len(departments) >= 1:
            context['departments'] = departments
        
        context['has_newsletter'] = True
        context['SITE_URL'] = 'Inicio'
        context['url'] = reverse('front:home')
        context['blog_post_test'] = [
            {
                'title':'Esto es un post',
                'sub_title':'New post 01',
                'text':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe ipsa nam facere fugiat maiores iste, placeat ratione consequuntur. Laboriosam in eos non dolores sit enim quaerat saepe exercitationem possimus ratione?',
                'background':'https://static.pexels.com/photos/261579/pexels-photo-261579.jpeg',
                'img':'/static/base/img/moby-background-01.jpg',
                'time_stamp':'01/01/2018',
                'slug':'new_post_1',
            },
            {
                'title':'Esto es un post',
                'sub_title':'New post 01',
                'text':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe ipsa nam facere fugiat maiores iste, placeat ratione consequuntur. Laboriosam in eos non dolores sit enim quaerat saepe exercitationem possimus ratione?',
                'background':'https://static.pexels.com/photos/261579/pexels-photo-261579.jpeg',
                'img':'/static/base/img/moby-background-01.jpg',
                'time_stamp':'01/01/2018',
                'slug':'new_post_2',
            },
            {
                'title':'Esto es un post',
                'sub_title':'New post 01',
                'text':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe ipsa nam facere fugiat maiores iste, placeat ratione consequuntur. Laboriosam in eos non dolores sit enim quaerat saepe exercitationem possimus ratione?',
                'background':'https://static.pexels.com/photos/261579/pexels-photo-261579.jpeg',
                'img':'/static/base/img/moby-background-01.jpg',
                'time_stamp':'01/01/2018',
                'slug':'new_post_3',
            }
        ]
        
        return context


class About(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/about.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Moby'
        return context


class Services(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/services.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Nuestros servicios'
        context['has_newsletter'] = True
        return context


class Contact(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/contact.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Contactanos'
        return context


class Search(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/search.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Buscar'
        return context
