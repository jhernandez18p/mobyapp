from django.conf import settings
from django.conf.urls import handler404,handler500,handler403,handler400
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views as flats
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views.static import serve

from app.urls import rest
from src.base import views as base_views

sitemaps = {
    'flatpages': FlatPageSitemap,
}

urlpatterns = [
    path('', include('src.base.urls', namespace='front')),
    path('social-ligin', include('social_django.urls', namespace='social')),
    path('blog/', include('src.blog.urls', namespace='blog')),
    path('servicios/', include('src.services.urls', namespace='services')),
    path('productos/', include('src.ventas.urls', namespace='sales')),
    path('intra/', include('src.intra.urls', namespace='intra')),
    path('auth/', include('src.user.urls',namespace='auth')),
    path('api/v2/', include('src.api.urls',namespace='api')),
    path('api/v2/auth/', include('knox.urls')),
    path('adminsite/', admin.site.urls),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT }),
    path('<path:url>', flats.flatpage),
]
    
admin.site.site_title = 'Dev2tech CMS'
admin.site.site_header = 'CMS Moby Supply'

handler404 = 'app.urls.views.page_not_found_view'
handler500 = 'app.urls.views.error_view'
handler403 = 'app.urls.views.permission_denied_view'
handler400 = 'app.urls.views.bad_request_view'
