from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView

from src.base.models import Carousel, CarouselImage
from .models import (Article, Photo, Department)
from .forms import PhotoForm
# Create your views here.

class Home(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/products.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        articles = Article.objects.all()
        if articles.exists():
            context['products'] = articles[0:9]

        products_header_carousel = Carousel.objects.all().filter(page_id=3).filter(position_id=1)
        if products_header_carousel.exists():
            context['products_header_carousel'] = True
            
            products_header_carousel_images = CarouselImage.objects.all().filter(Carousel_id=products_header_carousel[0].id)
            if products_header_carousel_images.exists():
                context['products_header_carousel_images'] = products_header_carousel_images
        
        departments = Department.objects.all()
        if departments.exists():
            context['departments'] = departments
        
        context['SITE_URL'] = 'Nuestros productos'
        context['has_newsletter'] = True
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


class Products_List(ListView):
    template_name = 'app/products_list.html'
    context = {}
    category = 'cat'
    paginate_by = 9
    queryset = ''
    
    context['SITE_URL'] = 'Departamento %s' % (category)
    context['cat'] = '%s' % (category)
    context['objects'] = {
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
        },10:{
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
        },11:{
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
        },12:{
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
        }
    }

def Products_Detail(request, slug):
    template = 'app/detail/product_details.html'
    context = {}
    category = 'herraje'
    context['SITE_URL'] = 'Detalle de producto'
    context['cat'] = '%s' % (category)
    context['object'] = {
        'name':'CUBIERTERO LINEA TEN DE 450 MM',
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
        'picture':'/static/base/img/logo.png',
    }
    return render(request, template, context)


class Departments(ListView):
    model = Department
    # context_object_name = 'boards'
    # queryset = ''
    template_name = 'app/departments.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Departamentos'
        context['objects'] = {}
        return context


class DepartmentDetail(DetailView):

    model = Department
    # context_object_name = 'boards'
    # queryset = ''
    template_name = 'app/detail/departments_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Detalles de Departamentos'
        context['objects'] = {}
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


class Providers(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/providers.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Proveedores'
        context['objects'] = {}
        return context


class ProvidersDetails(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/detail/provider_details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Detalles de proveedor'
        context['objects'] = {}
        return context