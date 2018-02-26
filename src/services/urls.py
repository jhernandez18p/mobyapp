from django.conf import settings
from django.contrib import admin
from django.contrib.flatpages import views as flats
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views.static import serve

from django.conf.urls.static import static

from src.base import views as base_views
from rest_framework import routers
from app.urls import rest

from django.urls import (path, re_path, include)
from .views import (
    Home,
    ServiceDetail,
    ServiceThanks,
    ServiceError,
)

app_name = 'services'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('/contacto/gracias', ServiceThanks.as_view(), name='thanks'),
    path('/contacto/error', ServiceError.as_view(), name='error'),
    path('/<slug:slug>', ServiceDetail.as_view(), name='detail'),
]