from django.urls import (path, re_path, include)
from .views import Home, Profile, Conf, Services,\
    Products, Support, Medias, Users, Blog,\
    BlogCreate, ConfCreate, MediaCreate,\
    UserCreate, ProductCreate, ServiceCreate,\
    BlogUpdate, ConfUpdate, MediaUpdate,\
    UserUpdate, ProductUpdate, ServiceUpdate,\
    BlogDelete, ConfDelete, MediaDelete,\
    UserDelete, ProductDelete, ServiceDelete
app_name = 'intra'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('blogs', Blog.as_view(), name='blog'),
    
    path('agregar/blog/', BlogCreate.as_view(), name='blog-create'),
    path('actualizar/blog/<int:pk>/', BlogUpdate.as_view(), name='blog-update'),
    path('eliminar/blog/<int:pk>/', BlogDelete.as_view(), name='blog-delete'),

    path('configuraciones', Conf.as_view(), name='conf'),
    
    path('agregar/configuraciones/', ConfCreate.as_view(), name='conf-create'),
    path('actualizar/configuraciones/<int:pk>/', ConfUpdate.as_view(), name='conf-update'),
    path('eliminar/configuraciones/<int:pk>/', ConfDelete.as_view(), name='conf-delete'),

    path('multimedias/', Medias.as_view(), name='medias'),
    
    path('agregar/multimedia/', MediaCreate.as_view(), name='media-create'),
    path('actualizar/multimedia/<int:pk>/', MediaUpdate.as_view(), name='media-update'),
    path('eliminar/multimedia/<int:pk>/', MediaDelete.as_view(), name='media-delete'),

    path('usuarios', Users.as_view(), name='users'),
    path('perfil', Profile.as_view(), name='profile'),
    
    path('agregar/usuario/', UserCreate.as_view(), name='user-create'),
    path('actualizar/usuario/<int:pk>/', UserUpdate.as_view(), name='user-update'),
    path('eliminar/usuario/<int:pk>/', UserDelete.as_view(), name='user-delete'),

    path('productos', Products.as_view(), name='products'),
    
    path('agregar/producto/', ProductCreate.as_view(), name='product-create'),
    path('actualizar/producto/<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('eliminar/producto/<int:pk>/', ProductDelete.as_view(), name='product-delete'),

    path('servicios', Services.as_view(), name='services'),
    
    path('agregar/servicio/', ServiceCreate.as_view(), name='service-create'),
    path('actualizar/servicio/<int:pk>/', ServiceUpdate.as_view(), name='service-update'),
    path('eliminar/servicio/<int:pk>/', ServiceDelete.as_view(), name='service-delete'),

    path('soporte', Support.as_view(), name='support'),
]