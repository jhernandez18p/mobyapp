from django.urls import (path, re_path, include)
from .views import (Home)

app_name = 'intra'
urlpatterns = [
    path('', Home.as_view(), name='home'),
]