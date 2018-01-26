from django.urls import (path, re_path, include)
from .views import (
    Home,
    Departments,
    Products_List,
    Products_Detail,
    BasicUploadView,
)

app_name = 'sales'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('detalle/<slug:slug>/', Products_Detail, name='product_detail'),
    path('departamentos/', Departments, name='departments'),
    path('departamento/<str:cat>/', Products_List, name='department_list'),
    path('proveedores/', Departments, name='providers'),
    path('proveedor/<str:prov>/', Departments, name='provider_detail'),
    path('subirfotos/', BasicUploadView.as_view(), name='basic_upload'),
]