from django.urls import (path, re_path, include)
from .views import (
    Home,
    ServiceDetail,
)

app_name = 'services'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('/<slug:slug>', ServiceDetail.as_view(), name='home'),
]