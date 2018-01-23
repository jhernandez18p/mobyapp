from django.urls import (path, re_path, include)
from .views import (
    Home,
    Departments,
    Products_List,
    Products_Detail,
)

app_name = 'sales'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('detalle/<slug:slug>/', Products_Detail, name='product_detail'),
    path('departamento/', Departments, name='departments'),
    path('departamento/<str:cat>/', Products_List, name='department_list'),
]