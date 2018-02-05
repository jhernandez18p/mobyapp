from django.urls import (path, re_path, include)
from .views import (
    Home,
    About,
    Services,
    Contact,
    Search,
)

app_name = 'front'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('contacto', Contact.as_view(), name='contact'),
    path('busqueda', Search.as_view(), name='search'),
]