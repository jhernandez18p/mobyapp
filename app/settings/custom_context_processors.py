from django.urls import reverse
from src.base.models import (Pages,Position,Site,SocialMedia)
from src.user.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail

from src.user.models import Profile
from src.blog.models import Post

def user(request):
    """
    Custom User Preprosessor
    """
    context = {}
    content = request
    ANONYMUS = False
    USER_FULLNAME = 'Unknow'
    USER_AVATAR = '/static/base/img/logo.png'

    try:
        current_user = content.user
        
        if current_user.is_anonymous:
            ANONYMUS = True
        else:
            ANONYMUS = False
        
        try:
            user_profile = current_user.profile
        except:
            Profile.objects.create(user=current_user)
            USER_FULLNAME = user_profile.get_fullname
            USER_AVATAR = user_profile.get_avatar
        
    except:
        ANONYMUS = False
        USER_FULLNAME = 'Unknow'
        USER_AVATAR = '/static/base/img/logo.png'

    context['ANONYMUS'] = ANONYMUS
    context['USER_FULLNAME'] = USER_FULLNAME
    context['USER_AVATAR'] = USER_AVATAR
    return context

def site(request):
    """
    Site info preprocessor 
    """
    context = {}
    context['SITE_TITLE'] = 'Moby Group'
    context['SITE_URL'] = 'Inicio'
    context['SITE_LOGO'] = '/static/base/img/logo.png'

    pages = Pages.objects.all()
    if not pages.exists():
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
    if not positions.exists():
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
        context['info_site'] = info_site[0]
        sm = SocialMedia.objects.filter(site=info_site[0].id)
        if sm.exists():
            context['social_media'] = sm
    else:
        info_site = Site(
            name='Moby Supply',
            description='',
            url='https://www.mobby-group.com',
        )
        info_site.save()

    blog_posts = Post.objects.all()[:5]
    if blog_posts.exists():
        context['blog_posts'] = blog_posts
    return context

def menu(request):
    """
    Menu preprocessor 
    """
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
    """
    Cookies prepeocessor
    """
    context = {}
    return context

