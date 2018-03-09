from django.urls import path, re_path, include
from .views import Home,Contact,Search,\
    ContactThanks,ContactError,session

app_name = 'front'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('contacto', Contact.as_view(), name='contact'),
    path('contacto/gracias', ContactThanks.as_view(), name='contact_thanks'),
    path('contacto/error', ContactError.as_view(), name='contact_error'),
    path('busqueda', Search.as_view(), name='search'),
    path('session', session, name='session'),
]