from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from src.base.models import Carousel, CarouselImage
from .models import (Article, Photo, Department, Provider, Brands, Category, Color)
from .forms import PhotoForm


class Home(ListView):
    queryset = ''
    template_name = 'app/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_URL'] = 'Nuestros productos'
        context['has_newsletter'] = True

        articles = Article.objects.all()
        if articles.exists():
            context['products'] = articles[:9]

        products_header_carousel = Carousel.objects.filter(Q(page_id=3) & Q(position_id=1))
        if products_header_carousel.exists():
            context['products_header_carousel'] = True
            
            products_header_carousel_images = CarouselImage.objects.filter(Carousel_id=products_header_carousel[0].id)
            if products_header_carousel_images.exists():
                context['products_header_carousel_images'] = products_header_carousel_images
        
        departments = Department.objects.all()
        if departments.exists():
            context['departments'] = departments[:4]

        brands = Brands.objects.all()
        if brands.exists():
            context['brands'] = brands

        context['url_nav'] = 'productos'
        return context


class ProductsList(ListView):

    model = Article
    template_name = 'app/products_list.html'
    paginate_by = 18
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        category = 'cat'
        context = super().get_context_data(**kwargs)
        context['SITE_URL'] = 'Departamento %s' % (category)
        context['cat'] = '%s' % (category)
        
        departments = Department.objects.all()
        if departments.exists():
            context['departments'] = departments
        
        categories = Category.objects.all()
        if categories.exists():
            context['categories'] = categories
        
        brands = Brands.objects.all()
        if brands.exists():
            context['brands'] = brands

        # print(context)
        context['url_nav'] = 'productos'
        return context


class ProductsDetail(DetailView):

    model = Article
    # queryset = ''
    template_name = 'app/detail/product_details.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        category = 'herraje'
        context['cat'] = '%s' % (category)
        context['SITE_URL'] = 'Detalle de producto'
        context['url_nav'] = 'productos'
        return context


class Departments(ListView):
    model = Department
    paginate_by = 4
    # context_object_name = 'boards'
    # queryset = ''
    template_name = 'app/departments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_URL'] = 'Departamentos'

        context['url_nav'] = 'productos'

        return context


class DepartmentDetail(DetailView):

    model = Department
    # context_object_name = 'boards'
    # queryset = ''
    template_name = 'app/detail/departments_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_URL'] = 'Detalles de Departamentos'
        # context['objects'] = {}
        articles = Article.objects.filter(department=self.get_object().pk)
        if articles.exists():
            context['products'] = articles[:9]
        context['url_nav'] = 'productos'
        return context


class BrandView(ListView):
    model = Brands
    # context_object_name = 'boards'
    paginate_by = 6
    # queryset = ''
    template_name = 'app/providers.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Proveedores'
        # context['objects'] = {}
        context['url_nav'] = 'productos'
        return context


class BrandsDetails(DetailView):
    model = Brands
    # context_object_name = 'boards'
    # queryset = ''
    template_name = 'app/detail/provider_details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(provider=self.get_object().pk)
        if articles.exists():
            print()
            context['products'] = articles[:9]
        context['SITE_URL'] = 'Detalles de proveedor'
        # context['objects'] = {}
        context['url_nav'] = 'productos'
        return context