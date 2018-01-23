from django.shortcuts import render
from django.views.generic import ListView, DetailView

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
        context['SITE_URL'] = 'Nuestros productos'
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
            },
        }
        return context


class Departments(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/products.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Departamentos'
        context['objects'] = {}
        return context

def Products_List(request, cat):
    template = 'app/products_list.html'
    context = {}
    category = cat
    
    context['SITE_URL'] = 'Categoría %s' % (category)
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
        },13:{
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
        },14:{
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
        },15:{
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
        },16:{
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
        },17:{
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
        },18:{
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
        },19:{
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
        },20:{
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
    return render(request, template, context)


def Products_Detail(request, slug):
    template = 'app/detail/product_details.html'
    context = {}
    category = 'herraje'
    context['SITE_URL'] = 'Detalle de producto'
    context['cat'] = '%s' % (category)
    context['object'] = {
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

