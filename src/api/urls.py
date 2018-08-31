from django.conf import settings
from django.conf.urls import handler404,handler500,handler403,handler400
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views as flats
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views.static import serve

from rest_framework import routers, views, serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_jwt.views import obtain_jwt_token

from src.api.views import viewset
from src.api.views.views import UserCreate

router = routers.DefaultRouter()
router.register(r'article', viewset.ArticleViewSet)
router.register(r'brands', viewset.BrandsViewSet)
router.register(r'carousel-image', viewset.FrontendCarouselImageViewSet)
router.register(r'carousel', viewset.FrontendCarouselViewSet)
router.register(r'category', viewset.CategoryViewSet)
router.register(r'color', viewset.ColorViewSet)
router.register(r'comments', viewset.BlogPostCommetViewSet)
router.register(r'department', viewset.DepartmentViewSet)
router.register(r'groups', viewset.GroupViewSet)
router.register(r'line', viewset.LineViewSet)
router.register(r'photo', viewset.PhotoViewSet)
router.register(r'posts', viewset.BlogPostViewSet)
router.register(r'provider', viewset.ProviderViewSet)
router.register(r'services', viewset.ServiceViewSet)
router.register(r'site', viewset.SiteViewSet)
router.register(r'subLine', viewset.SubLineViewSet)
router.register(r'type', viewset.TypeViewSet)
router.register(r'users', viewset.UserViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    # Token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/auth/', obtain_jwt_token),
    # Auth
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/register/', UserCreate.as_view(), name='register'),
    # path('/', include('rest_framework.urls', namespace='rest_framework')),
]