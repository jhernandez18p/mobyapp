from django.urls import (path, re_path, include)
from django.views.decorators.cache import cache_page
from .views import (
    Home,
    About,
    Services,
    Contact,
    Search,
    ContactThanks,
    ContactError,
    session
)

app_name = 'front'
urlpatterns = [
    path('', cache_page(60*60)(Home.as_view()), name='home'),
    path('contacto', cache_page(60*60)(Contact.as_view()), name='contact'),
    path('contacto/gracias', ContactThanks.as_view(), name='contact_thanks'),
    path('contacto/error', ContactError.as_view(), name='contact_error'),
    path('busqueda', Search.as_view(), name='search'),
    path('session', session, name='session'),
]