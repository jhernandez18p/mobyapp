from django.urls import (path, re_path, include)
from .views import (
    Home,
    Departments,
    DepartmentDetail,
    ProductsList,
    ProductsDetail,
    Providers,
    ProvidersDetails,
)

app_name = 'sales'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('/todos', ProductsList.as_view(), name='all'),
    path('/detalle/<slug:slug>', ProductsDetail.as_view(), name='product_detail'),
    
    path('/departamentos', Departments.as_view(), name='departments'),
    path('/departamento/<slug:slug>', DepartmentDetail.as_view(), name='department_detail'),

    path('/proveedores', Providers.as_view(), name='providers'),
    path('/proveedor/<slug:slug>', ProvidersDetails.as_view(), name='provider_detail'),
]