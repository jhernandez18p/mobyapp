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
from src.api.views.views import UserCreate, LoginAPI, UserAPI, CheckEmail, CheckUsername

router = routers.DefaultRouter()
router.register(r'answers', viewset.AnswersViewSet)
router.register(r'brands', viewset.BrandsViewSet)
router.register(r'carousel-images', viewset.FrontendCarouselImageViewSet)
router.register(r'carousels', viewset.FrontendCarouselViewSet)
router.register(r'categories', viewset.CategoryViewSet)
router.register(r'colors', viewset.ColorViewSet)
router.register(r'comments', viewset.BlogPostCommetViewSet)
router.register(r'departments', viewset.DepartmentViewSet)
router.register(r'flatpages', viewset.FlatpagesViewSet)
router.register(r'groups', viewset.GroupViewSet)
router.register(r'lines', viewset.LineViewSet)
router.register(r'page-positions', viewset.PositionViewSet)
router.register(r'flat-pages', viewset.FlatpagesViewSet)
router.register(r'pages', viewset.PagesViewSet)
router.register(r'photos', viewset.PhotoViewSet)
router.register(r'posts', viewset.PublicBlogPostViewSet)
router.register(r'products', viewset.ArticleViewSet)
router.register(r'providers', viewset.ProviderViewSet)
router.register(r'questions', viewset.QuestionsViewSet)
router.register(r'services', viewset.ServiceViewSet)
router.register(r'site', viewset.SiteViewSet)
router.register(r'social-media', viewset.SocialMediaViewSet)
router.register(r'sub-lines', viewset.SubLineViewSet)
router.register(r'tags', viewset.BlogTagViewSet)
router.register(r'testimonials', viewset.TestimonialViewSet)
router.register(r'types', viewset.TypeViewSet)
router.register(r'types', viewset.TypeViewSet)
router.register(r'users', viewset.UserViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    # Token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/auth/', obtain_jwt_token),
    # Auth
    path('auth/login/', LoginAPI.as_view(), name='token_obtain_pair'),
    path('auth/register/', UserCreate.as_view(), name='register'),
    path('auth/user/', UserAPI.as_view(), name='register'),
    path('auth/check-email/', CheckEmail, name='register'),
    path('auth/check-username/', CheckUsername, name='register'),
    # path('/', include('rest_framework.urls', namespace='rest_framework')),
]