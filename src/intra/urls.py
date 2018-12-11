from django.urls import (path, re_path, include)
from src.intra.views import *

app_name = 'intra'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    
    path('blogs', Blog.as_view(), name='blog'),
    path('agregar/blog/', BlogCreate.as_view(), name='blog-create'),
    path('actualizar/blog/<int:pk>/', BlogUpdate.as_view(), name='blog-update'),
    path('eliminar/blog/<int:pk>/', BlogDelete.as_view(), name='blog-delete'),

    path('comentarios', Blog.as_view(), name='comments'),
    path('agregar/comentario/', BlogCreate.as_view(), name='comment-create'),
    path('actualizar/comentario/<int:pk>/', BlogUpdate.as_view(), name='comment-update'),
    path('eliminar/comentario/<int:pk>/', BlogDelete.as_view(), name='comment-delete'),

    path('configuraciones', Conf.as_view(), name='conf'),
    path('agregar/configuraciones/', ConfCreate.as_view(), name='conf-create'),
    path('actualizar/configuraciones/<int:pk>/', ConfUpdate.as_view(), name='conf-update'),
    path('eliminar/configuraciones/<int:pk>/', ConfDelete.as_view(), name='conf-delete'),

    path('multimedias/', Medias.as_view(), name='medias'),
    path('agregar/multimedia/', MediaCreate.as_view(), name='media-create'),
    path('actualizar/multimedia/<int:pk>/', MediaUpdate.as_view(), name='media-update'),
    path('eliminar/multimedia/<int:pk>/', MediaDelete.as_view(), name='media-delete'),

    path('perfil', Profile.as_view(), name='profile'),
    path('usuarios', Users.as_view(), name='users'),
    path('agregar/usuario/', UserCreate.as_view(), name='user-create'),
    path('actualizar/usuario/<int:pk>/', UserUpdate.as_view(), name='user-update'),
    path('eliminar/usuario/<int:pk>/', UserDelete.as_view(), name='user-delete'),

    path('productos', Products.as_view(), name='products'),
    path('productos/lineas', ProductLines.as_view(), name='products-lines'),
    path('productos/sub-lineas', ProductSubLines.as_view(), name='products-sublines'),
    path('productos/colores', ProductColor.as_view(), name='products-colors'),
    path('productos/marcas', ProductBrand.as_view(), name='products-brands'),
    path('productos/categorias', ProductCategory.as_view(), name='products-categories'),
    path('productos/departamentos', ProductDepartment.as_view(), name='products-departments'),

    path('agregar/producto/', ProductCreate.as_view(), name='product-create'),
    path('actualizar/producto/<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('eliminar/producto/<int:pk>/', ProductDelete.as_view(), name='product-delete'),

    path('servicios', Services.as_view(), name='services'),
    
    path('agregar/servicio/', ServiceCreate.as_view(), name='service-create'),
    path('actualizar/servicio/<int:pk>/', ServiceUpdate.as_view(), name='service-update'),
    path('eliminar/servicio/<int:pk>/', ServiceDelete.as_view(), name='service-delete'),

    path('soporte', Support.as_view(), name='support'),
]