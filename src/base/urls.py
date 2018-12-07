from django.urls import path, re_path, include
from .views import Home,Contact,Search,\
    ContactThanks,ContactError,session

app_name = 'front'
urlpatterns = [
    # path('', Home, name='home'),
    path('', Home.as_view(), name='home'),
    # path('contacto/gracias', Home, name='contact_thanks'),
    path('contacto/gracias', ContactThanks.as_view(), name='contact_thanks'),
    # path('contacto', Home, name='contact'),
    path('contacto', Contact.as_view(), name='contact'),
    # path('contacto/error', Home, name='contact_error'),
    path('contacto/error', ContactError.as_view(), name='contact_error'),
    # path('busqueda', Home, name='search'),
    path('busqueda', Search.as_view(), name='search'),
    # path('session', Home, name='session'),
    path('session', session, name='session'),
]