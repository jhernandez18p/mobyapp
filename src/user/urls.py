from django.urls import (path, re_path, include)
from .views import (Login,Logout,Register, activate)

app_name = 'auth'
urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('register', Register.as_view(), name='register'),
    re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$', activate, name='activate'),
]