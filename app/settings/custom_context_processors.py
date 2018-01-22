from django.urls import reverse

def site(request):
    # Site info preprocessor 
    context = {}
    context['SITE_TITLE'] = 'Moby Group'
    context['SITE_URL'] = ''
    context['SITE_LOGO'] = '/static/base/img/logo.png'
    return context

def menu(request):
    # Menu preprocessor 
    context = {}
    menu = [
        {'name':'inicio','url':reverse('front:home'),'have_icon':False},
        {'name':'servicios','url':reverse('front:services'),'have_icon':False},
        {'name':'productos','url':reverse('sales:home'),'have_icon':False},
        {'name':'blog','url':reverse('blog:home'),'have_icon':False},
        {'name':'contacto','url':reverse('front:contact'),'have_icon':False},
        {'name':'search','url':reverse('front:search'),'have_icon':True}
    ]
    context['FRONT_HEADER_MENU'] = menu
    return context


def sessions(request):
    # Cookies prepeocessor
    context = {}
    return context