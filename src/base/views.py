from django.shortcuts import render
from django.views.generic import ListView, DetailView

class Home(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Inicio'
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
        return context


class Products(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/products.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Nuestros productos'
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


def Products_Detail(request, cat , slug):
    template = 'app/detail/product_details.html'
    context = {}
    category = cat
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
        'picture':'/static/base/img/art.png',
    }
    return render(request, template, context)


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


class Blog(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/blog.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Ultimas noticias'
        context['objects'] = {
            1:{
                'title':'Esto es un post',
                'sub_title':'New post 01',
                'text':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe ipsa nam facere fugiat maiores iste, placeat ratione consequuntur. Laboriosam in eos non dolores sit enim quaerat saepe exercitationem possimus ratione?',
                'background':'https://static.pexels.com/photos/261579/pexels-photo-261579.jpeg',
                'img':'/static/base/img/food.jpg',
                'time_stamp':'01/01/2018',
                'slug':'new_post_1',
            },
            2:{
                'title':'Esto es un post',
                'sub_title':'New post 01',
                'text':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe ipsa nam facere fugiat maiores iste, placeat ratione consequuntur. Laboriosam in eos non dolores sit enim quaerat saepe exercitationem possimus ratione?',
                'background':'https://static.pexels.com/photos/261579/pexels-photo-261579.jpeg',
                'img':'/static/base/img/food.jpg',
                'time_stamp':'01/01/2018',
                'slug':'new_post_2',
            },
            3:{
                'title':'Esto es un post',
                'sub_title':'New post 01',
                'text':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe ipsa nam facere fugiat maiores iste, placeat ratione consequuntur. Laboriosam in eos non dolores sit enim quaerat saepe exercitationem possimus ratione?',
                'background':'https://static.pexels.com/photos/261579/pexels-photo-261579.jpeg',
                'img':'/static/base/img/food.jpg',
                'time_stamp':'01/01/2018',
                'slug':'new_post_3',
            }
        }
        return context


def Blog_Detail(request, slug='new_post'):

    template = 'app/detail/blog_detail.html'
    context = {}

    context['SITE_URL'] = 'Ultimas noticias'
    context['object'] = {
        'title':'Esto es un post',
        'sub_title':'New post 01',
        'text':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe ipsa nam facere fugiat maiores iste, placeat ratione consequuntur. Laboriosam in eos non dolores sit enim quaerat saepe exercitationem possimus ratione?',
        'background':'https://static.pexels.com/photos/261579/pexels-photo-261579.jpeg',
        'img':'/static/base/img/food.jpg',
        'time_stamp':'01/01/2018'
    }
    return render(request, template, context)


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
