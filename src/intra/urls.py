from django.urls import (path, re_path, include)
from src.intra.views.base import *
from src.intra.views.blog import *
from src.intra.views.multimedia import *
from src.intra.views.sales import *
from src.intra.views.services import *
from src.intra.views.support import *
from src.intra.views.users import *

app_name = 'intra'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    
    path('blogs', Blog.as_view(), name='blog'),
    path('my-posts', MyBlog.as_view(), name='my-blog'),
    path('agregar/blog', BlogCreate.as_view(), name='blog-create'),
    path('actualizar/blog/<int:pk>/', BlogUpdate.as_view(), name='blog-update'),
    path('eliminar/blog/<int:pk>/', BlogDelete.as_view(), name='blog-delete'),

    path('comentarios', Comments.as_view(), name='comments'),
    path('agregar/comentario', CommentCreate.as_view(), name='comment-create'),
    path('actualizar/comentario/<int:pk>/', CommentUpdate.as_view(), name='comment-update'),
    path('eliminar/comentario/<int:pk>/', CommentDelete.as_view(), name='comment-delete'),

    path('etiquetas', Tags.as_view(), name='tags'),
    path('agregar/etiqueta', TagCreate.as_view(), name='tag-create'),
    path('actualizar/etiqueta/<int:pk>/', TagUpdate.as_view(), name='tag-update'),
    path('eliminar/etiqueta/<int:pk>/', TagDelete.as_view(), name='tag-delete'),

    path('configuraciones', Conf.as_view(), name='conf'),
    path('agregar/configuraciones', ConfCreate.as_view(), name='conf-create'),
    path('actualizar/configuraciones/<int:pk>/', ConfUpdate.as_view(), name='conf-update'),
    path('eliminar/configuraciones/<int:pk>/', ConfDelete.as_view(), name='conf-delete'),
    
    path('configuraciones/paginas', ConfPages.as_view(), name='conf-pages'),
    path('agregar/pagina', ConfPageCreate.as_view(), name='conf-page-create'),
    path('actualizar/pagina/<int:pk>/', ConfPageUpdate.as_view(), name='conf-page-update'),
    path('eliminar/pagina/<int:pk>/', ConfPageDelete.as_view(), name='conf-page-delete'),

    path('configuraciones/carruseles', ConfSlides.as_view(), name='conf-slides'),
    path('agregar/carrusel', ConfSlideCreate.as_view(), name='conf-slide-create'),
    path('actualizar/carrusel/<int:pk>/', ConfSlideUpdate.as_view(), name='conf-slide-update'),
    path('eliminar/carrusel/<int:pk>/', ConfSlideDelete.as_view(), name='conf-slide-delete'),
    path('agregar/carrusel-image', ConfSlideImgCreate.as_view(), name='conf-slide-img-create'),
    path('actualizar/carrusel-image/<int:pk>/', ConfSlideImgUpdate.as_view(), name='conf-slide-img-update'),
    path('eliminar/carrusel-image/<int:pk>/', ConfSlideImgDelete.as_view(), name='conf-slide-img-delete'),

    path('configuraciones/faq', ConfFAQS.as_view(), name='conf-faqs'),
    path('agregar/pregunta', ConfFAQQuestionCreate.as_view(), name='conf-faq-question-create'),
    path('actualizar/pregunta/<int:pk>/', ConfFAQQuestionUpdate.as_view(), name='conf-faq-question-update'),
    path('eliminar/pregunta/<int:pk>/', ConfFAQQuestionDelete.as_view(), name='conf-faq-question-delete'),
    path('agregar/respuesta', ConfFAQAnswerCreate.as_view(), name='conf-faq-answer-create'),
    path('actualizar/respuesta/<int:pk>/', ConfFAQAnswerUpdate.as_view(), name='conf-faq-answer-update'),
    path('eliminar/respuesta/<int:pk>/', ConfFAQAnswerDelete.as_view(), name='conf-faq-answer-delete'),

    path('configuraciones/newsletters', ConfNewsletters.as_view(), name='conf-newsletters'),
    path('agregar/newsletter', ConfNewsletterCreate.as_view(), name='conf-newsletter-create'),
    path('actualizar/newsletter/<int:pk>/', ConfNewsletterUpdate.as_view(), name='conf-newsletter-update'),
    path('eliminar/newsletter/<int:pk>/', ConfNewsletterDelete.as_view(), name='conf-newsletter-delete'),

    path('multimedias/', Medias.as_view(), name='medias'),
    path('agregar/multimedia', MediaCreate.as_view(), name='media-create'),
    path('actualizar/multimedia/<int:pk>/', MediaUpdate.as_view(), name='media-update'),
    path('eliminar/multimedia/<int:pk>/', MediaDelete.as_view(), name='media-delete'),

    path('perfil', Profile.as_view(), name='profile'),
    path('usuarios', Users.as_view(), name='users'),
    path('agregar/usuario', UserCreate.as_view(), name='user-create'),
    path('actualizar/usuario/<int:pk>/', UserUpdate.as_view(), name='user-update'),
    path('eliminar/usuario/<int:pk>/', UserDelete.as_view(), name='user-delete'),

    path('productos', Products.as_view(), name='products'),
    path('productos/top', TopProducts.as_view(), name='products-top'),
    path('agregar/producto', ProductCreate.as_view(), name='product-create'),
    path('actualizar/producto/<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('eliminar/producto/<int:pk>/', ProductDelete.as_view(), name='product-delete'),

    path('productos/lineas', ProductLines.as_view(), name='products-lines'),
    path('agregar/linea', LineCreate.as_view(), name='line-create'),
    path('actualizar/linea/<int:pk>/', LineUpdate.as_view(), name='line-update'),
    path('eliminar/linea/<int:pk>/', LineDelete.as_view(), name='line-delete'),

    path('productos/sub-lineas', ProductSubLines.as_view(), name='products-sublines'),
    path('agregar/sublinea/', SubLineCreate.as_view(), name='subline-create'),
    path('actualizar/sub-linea/<int:pk>/', SubLineUpdate.as_view(), name='subline-update'),
    path('eliminar/sub-linea/<int:pk>/', SubLineDelete.as_view(), name='subline-delete'),
    
    path('productos/colores', ProductColor.as_view(), name='products-colors'),
    path('agregar/color', ColorCreate.as_view(), name='color-create'),
    path('actualizar/color/<int:pk>/', ColorUpdate.as_view(), name='color-update'),
    path('eliminar/color/<int:pk>/', ColorDelete.as_view(), name='color-delete'),
    
    path('productos/marcas', ProductBrand.as_view(), name='products-brands'),
    path('agregar/marca', BrandCreate.as_view(), name='brand-create'),
    path('actualizar/marca/<int:pk>/', BrandUpdate.as_view(), name='brand-update'),
    path('eliminar/marca/<int:pk>/', BrandDelete.as_view(), name='brand-delete'),
    
    path('productos/categorias', ProductCategory.as_view(), name='products-categories'),
    path('agregar/categoria', CategoryCreate.as_view(), name='category-create'),
    path('actualizar/categoria/<int:pk>/', CategoryUpdate.as_view(), name='category-update'),
    path('eliminar/categoria/<int:pk>/', CategoryDelete.as_view(), name='category-delete'),
    
    path('productos/departamentos', ProductDepartment.as_view(), name='products-departments'),
    path('agregar/departamento', DepartmentCreate.as_view(), name='department-create'),
    path('actualizar/departamento/<int:pk>/', DepartmentUpdate.as_view(), name='department-update'),
    path('eliminar/departamento/<int:pk>/', DepartmentDelete.as_view(), name='department-delete'),

    path('servicios', Services.as_view(), name='services'),    
    path('agregar/servicio', ServiceCreate.as_view(), name='service-create'),
    path('actualizar/servicio/<int:pk>/', ServiceUpdate.as_view(), name='service-update'),
    path('eliminar/servicio/<int:pk>/', ServiceDelete.as_view(), name='service-delete'),
    path('agregar/servicio-img', ServiceIMGCreate.as_view(), name='service-img-create'),
    path('actualizar/servicio-img/<int:pk>/', ServiceIMGUpdate.as_view(), name='service-img-update'),
    path('eliminar/servicio-img/<int:pk>/', ServiceIMGDelete.as_view(), name='service-img-delete'),

    path('soporte', Support.as_view(), name='support'),
]