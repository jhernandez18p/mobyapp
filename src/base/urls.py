from django.urls import (path, re_path, include)
from .views import (
    Home,
    About,
    Services,
    Products,
    Products_List,
    Products_Detail,
    Contact,
    Search,
    Blog,
    Blog_Detail
)

app_name = 'front'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('servicios/', Services.as_view(), name='services'),
    path('productos/', Products.as_view(), name='products'),
    path('productos/<str:cat>/', Products_List, name='products_list'),
    path('productos/<str:cat>/<slug:slug>/', Products_Detail, name='product_detail'),
    path('blog/', Blog.as_view(), name='blog'),
    path('blog/<slug:slug>/', Blog_Detail, name='blog_detail'),
    path('contacto/', Contact.as_view(), name='contact'),
    path('busqueda/', Search.as_view(), name='search'),
]