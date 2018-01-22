from django.urls import (path, re_path, include)
from .views import (
    Home,
    Products_List,
    Products_Detail,
)

app_name = 'sales'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('<str:cat>/', Products_List, name='products_list'),
    path('detalle/<slug:slug>/', Products_Detail, name='product_detail'),
]