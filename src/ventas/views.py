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
            print()
            context['products'] = articles[:9]
        context['products_test'] = {
            1:{
                'co_art':'113120',
                'art_des':'CUBIERTERO LINEA TEN DE 450 MM',
                'co_lin':'HERR',
                'co_cat':'VARIOS',
                'co_subl':'VRO',
                'co_color':'10',
                'CO_CATW':'',
                'ref':'',
                'modelo':'',
                'procedenci':'1',
                'co_prov':'P00049',
                'uni_venta':'PZA',
                'sstock_act':'10',
                'prec_vta1':'7.2',
                'prec_vta2':'8',
                'prec_vta3':'9.2',
                'prec_vta4':'12.42',
                'prec_vta5':'9.2',
                'tipo':'V',
                'picture':'/static/base/img/art.png',
            },2:{
                'co_art':'113120',
                'art_des':'CUBIERTERO LINEA TEN DE 450 MM',
                'co_lin':'HERR',
                'co_cat':'VARIOS',
                'co_subl':'VRO',
                'co_color':'10',
                'CO_CATW':'',
                'ref':'',
                'modelo':'',
                'procedenci':'1',
                'co_prov':'P00049',
                'uni_venta':'PZA',
                'sstock_act':'10',
                'prec_vta1':'7.2',
                'prec_vta2':'8',
                'prec_vta3':'9.2',
                'prec_vta4':'12.42',
                'prec_vta5':'9.2',
                'tipo':'V',
                'picture':'/static/base/img/art.png',
            },3:{
                'co_art':'113120',
                'art_des':'CUBIERTERO LINEA TEN DE 450 MM',
                'co_lin':'HERR',
                'co_cat':'VARIOS',
                'co_subl':'VRO',
                'co_color':'10',
                'CO_CATW':'',
                'ref':'',
                'modelo':'',
                'procedenci':'1',
                'co_prov':'P00049',
                'uni_venta':'PZA',
                'sstock_act':'10',
                'prec_vta1':'7.2',
                'prec_vta2':'8',
                'prec_vta3':'9.2',
                'prec_vta4':'12.42',
                'prec_vta5':'9.2',
                'tipo':'V',
                'picture':'/static/base/img/art.png',
            },4:{
                'co_art':'113120',
                'art_des':'CUBIERTERO LINEA TEN DE 450 MM',
                'co_lin':'HERR',
                'co_cat':'VARIOS',
                'co_subl':'VRO',
                'co_color':'10',
                'CO_CATW':'',
                'ref':'',
                'modelo':'',
                'procedenci':'1',
                'co_prov':'P00049',
                'uni_venta':'PZA',
                'sstock_act':'10',
                'prec_vta1':'7.2',
                'prec_vta2':'8',
                'prec_vta3':'9.2',
                'prec_vta4':'12.42',
                'prec_vta5':'9.2',
                'tipo':'V',
                'picture':'/static/base/img/art.png',
            },5:{
                'co_art':'113120',
                'art_des':'CUBIERTERO LINEA TEN DE 450 MM',
                'co_lin':'HERR',
                'co_cat':'VARIOS',
                'co_subl':'VRO',
                'co_color':'10',
                'CO_CATW':'',
                'ref':'',
                'modelo':'',
                'procedenci':'1',
                'co_prov':'P00049',
                'uni_venta':'PZA',
                'sstock_act':'10',
                'prec_vta1':'7.2',
                'prec_vta2':'8',
                'prec_vta3':'9.2',
                'prec_vta4':'12.42',
                'prec_vta5':'9.2',
                'tipo':'V',
                'picture':'/static/base/img/art.png',
            },6:{
                'co_art':'113120',
                'art_des':'CUBIERTERO LINEA TEN DE 450 MM',
                'co_lin':'HERR',
                'co_cat':'VARIOS',
                'co_subl':'VRO',
                'co_color':'10',
                'CO_CATW':'',
                'ref':'',
                'modelo':'',
                'procedenci':'1',
                'co_prov':'P00049',
                'uni_venta':'PZA',
                'sstock_act':'10',
                'prec_vta1':'7.2',
                'prec_vta2':'8',
                'prec_vta3':'9.2',
                'prec_vta4':'12.42',
                'prec_vta5':'9.2',
                'tipo':'V',
                'picture':'/static/base/img/art.png',
            },7:{
                'co_art':'113120',
                'art_des':'CUBIERTERO LINEA TEN DE 450 MM',
                'co_lin':'HERR',
                'co_cat':'VARIOS',
                'co_subl':'VRO',
                'co_color':'10',
                'CO_CATW':'',
                'ref':'',
                'modelo':'',
                'procedenci':'1',
                'co_prov':'P00049',
                'uni_venta':'PZA',
                'sstock_act':'10',
                'prec_vta1':'7.2',
                'prec_vta2':'8',
                'prec_vta3':'9.2',
                'prec_vta4':'12.42',
                'prec_vta5':'9.2',
                'tipo':'V',
                'picture':'/static/base/img/art.png',
            },8:{
                'co_art':'113120',
                'art_des':'CUBIERTERO LINEA TEN DE 450 MM',
                'co_lin':'HERR',
                'co_cat':'VARIOS',
                'co_subl':'VRO',
                'co_color':'10',
                'CO_CATW':'',
                'ref':'',
                'modelo':'',
                'procedenci':'1',
                'co_prov':'P00049',
                'uni_venta':'PZA',
                'sstock_act':'10',
                'prec_vta1':'7.2',
                'prec_vta2':'8',
                'prec_vta3':'9.2',
                'prec_vta4':'12.42',
                'prec_vta5':'9.2',
                'tipo':'V',
                'picture':'/static/base/img/art.png',
            },9:{
                'co_art':'113120',
                'art_des':'CUBIERTERO LINEA TEN DE 450 MM',
                'co_lin':'HERR',
                'co_cat':'VARIOS',
                'co_subl':'VRO',
                'co_color':'10',
                'CO_CATW':'',
                'ref':'',
                'modelo':'',
                'procedenci':'1',
                'co_prov':'P00049',
                'uni_venta':'PZA',
                'sstock_act':'10',
                'prec_vta1':'7.2',
                'prec_vta2':'8',
                'prec_vta3':'9.2',
                'prec_vta4':'12.42',
                'prec_vta5':'9.2',
                'tipo':'V',
                'picture':'/static/base/img/art.png',
            },
        }
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
        return context