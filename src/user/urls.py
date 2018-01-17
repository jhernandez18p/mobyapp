from django.urls import (path, re_path, include)
from .views import (Login,Logout,Register)

app_name = 'auth'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
]