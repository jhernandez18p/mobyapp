from django.urls import (path, re_path, include)
from .views import (Login,Logout,Register, activate, modal_cookie)

app_name = 'auth'
urlpatterns = [
    path('/modal', modal_cookie, name='modal-cookie'),
    path('/login/', Login.as_view(), name='login'),
    path('/logout/', Logout.as_view(), name='logout'),
    path('/register/', Register, name='register'),
    re_path('/activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$', activate, name='activate'),
]