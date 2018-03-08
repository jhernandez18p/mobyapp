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
    path('todos/', ProductsList.as_view(), name='all'),
    path('detalles/<slug:slug>', ProductsDetail.as_view(), name='product_detail'),
    
    path('departamentos/', Departments.as_view(), name='departments'),
    path('departamentos/<slug:slug>', DepartmentDetail.as_view(), name='department_detail'),

    path('marcas/', Providers.as_view(), name='brands'),
    path('marcas/<slug:slug>', ProvidersDetails.as_view(), name='brand_detail'),
]