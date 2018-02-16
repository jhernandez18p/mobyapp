from django.urls import (path, re_path, include)
from .views import (
    Home,
    Departments,
    DepartmentDetail,
    Products_List,
    Products_Detail,
    Providers,
    ProvidersDetails,
)

app_name = 'sales'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('/todos', Products_List.as_view(), name='all'),
    path('/detalle/<slug:slug>', Products_Detail.as_view(), name='product_detail'),
    
    path('/departamentos', Departments.as_view(), name='departments'),
    path('/departamento/<str:slug>', DepartmentDetail.as_view(), name='department_detail'),

    path('/proveedores', Providers.as_view(), name='providers'),
    path('/proveedor/<str:prov>', ProvidersDetails.as_view(), name='provider_detail'),
]