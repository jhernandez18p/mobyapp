from django.urls import (path, re_path, include)
from .views import (custom_login,custom_logout,custom_register, activate, modal_cookie,error, thanks)

app_name = 'auth'
urlpatterns = [
    path('/modal', modal_cookie, name='modal-cookie'),
    path('/error', error, name='error'),
    path('/gracias', thanks, name='thanks'),
    path('/login/', custom_login, name='login'),
    path('/logout/', custom_logout, name='logout'),
    path('/register/', custom_register, name='register'),
    re_path('/activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$', activate, name='activate'),
]