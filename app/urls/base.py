from django.conf import settings
from django.contrib import admin
from django.contrib.flatpages import views as flats
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.flatpages import views
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.views.static import serve

from src.base import views as base_views
from rest_framework import routers
from app.urls import rest

from app.urls import error

router = routers.DefaultRouter()
router.register(r'users', rest.UserViewSet)
router.register(r'groups', rest.GroupViewSet)

sitemaps = {
    'flatpages': FlatPageSitemap,
}

handler404 = error.page_not_found_view
handler500 = error.error_view
handler403 = error.permission_denied_view
handler400 = error.bad_request_view

urlpatterns = [
    path('', include('src.base.urls', namespace='front')),
    path('social-ligin/', include('social_django.urls', namespace='social')),
    path('blog', include('src.blog.urls', namespace='blog')),
    path('servicios', include('src.services.urls', namespace='services')),
    path('productos', include('src.ventas.urls', namespace='sales')),
    path('intra', include('src.intra.urls', namespace='intra')),
    path('auth', include('src.user.urls',namespace='auth')),
    path('adminsite/', admin.site.urls),
    path('api', include(router.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/auth', include('rest_framework.urls', 
        namespace='rest_framework')),
    path('sitemap.xml', sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('<path:url>/', views.flatpage),
]

if settings.DEBUG:
    urlpatterns += [
        re_path('^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

admin.site.site_title = 'Dev2tech CMS'
admin.site.site_header = 'CMS Moby Supply'