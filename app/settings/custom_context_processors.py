from django.urls import reverse
from src.base.models import (Pages,Position,Site,SocialMedia)
from src.user.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail

from src.user.models import Profile

def site(request):
    # Site info preprocessor 
    context = {}
    context['SITE_TITLE'] = 'Moby Group'
    context['SITE_URL'] = ''
    context['SITE_LOGO'] = '/static/base/img/logo.png'

    user = request.user

    if user.is_anonymous:
        print('AnonymousUser')
    else:
        if request.user.profile.get_fullname:
            context['USER_FULLNAME'] = request.user.profile.get_fullname

        if request.user.profile.get_avatar:
            context['USER_AVATAR'] = request.user.profile.get_avatar


    pages = Pages.objects.all()
    if pages.exists():
        pass
    else:
        new_pages = [
            {'name':'inicio','url':reverse('front:home'),'have_icon':False},
            {'name':'servicios','url':reverse('services:home'),'have_icon':False},
            {'name':'productos','url':reverse('sales:home'),'have_icon':False},
            {'name':'blog','url':reverse('blog:home'),'have_icon':False},
            {'name':'contacto','url':reverse('front:contact'),'have_icon':False},
            {'name':'search','url':reverse('front:search'),'have_icon':True}
        ]
        for object_list in new_pages:
            new_page = Pages(
                name=object_list['name'],
                url=object_list['url'],
                have_icon=object_list['have_icon']
            )
            new_page.save()

    positions = Position.objects.all()
    if positions.exists():
        pass
    else:
        default_positions = [
            {'name':'header','description':''},
            {'name':'section','description':''},
            {'name':'footer','description':''},
        ]
        for object_list in default_positions:
            new_position = Position(
                name=object_list['name'],
                description=object_list['description'],
            )
            new_position.save()

    info_site = Site.objects.filter(id=1)
    if info_site.exists():
        # context['site_short_desc'] = info_site[0].short_description
        # context['site_email'] = info_site[0].email
        # context['site_email2'] = info_site[0].email2
        # context['site_phone'] = info_site[0].phone
        # context['site_phone2'] = info_site[0].phone2
        # context['site_schedule'] = info_site[0].schedule
        # context['site_workday'] = info_site[0].workday
        # context['site_address'] = info_site[0].address
        context['info_site'] = info_site[0]
        sm = SocialMedia.objects.filter(site=info_site[0].id)
        if sm.exists():
            context['social_media'] = sm
        pass
    else:
        info_site = Site(
            name='Moby Supply',
            description='',
            url='https://www.mobby-group.com',
        )
        info_site.save()
    return context

def menu(request):
    # Menu preprocessor 
    context = {}
    menu = [
        {'name':'inicio','url':reverse('front:home'),'have_icon':False},
        {'name':'servicios','url':reverse('services:home'),'have_icon':False},
        {'name':'productos','url':reverse('sales:home'),'have_icon':False},
        {'name':'blog','url':reverse('blog:home'),'have_icon':False},
        {'name':'contacto','url':reverse('front:contact'),'have_icon':False},
        # {'name':'search','url':reverse('front:search'),'have_icon':True}
    ]

    if 'cookie_modal' in request.COOKIES:
        context['cookie_modal'] = False
    else:
        context['cookie_modal'] = True
        

    context['FRONT_HEADER_MENU'] = menu
    return context


def sessions(request):
    # Cookies prepeocessor
    context = {}
    return context