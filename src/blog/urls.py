from django.urls import (path, re_path, include)
from .views import (
    Home,
    BlogDetail,
    comment_create,
)

app_name = 'blog'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('gracias/', Home.as_view(), name='thanks'),
    path('<slug:slug>/', BlogDetail.as_view(), name='blog_detail'),
    path('<slug:slug>/comentario/crear/', comment_create, name='add_comment'),
]