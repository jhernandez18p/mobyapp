from django.urls import (path, re_path, include)
from .views import (Home,About,Services,Products,Contact,Search, Blog)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('quienes-somos/', About.as_view(), name='about'),
    path('servicios/', Services.as_view(), name='services'),
    path('productos/', Products.as_view(), name='products'),
    path('blog/', Blog.as_view(), name='blog'),
    path('contacto/', Contact.as_view(), name='contact'),
    path('busqueda/', Search.as_view(), name='search'),
]