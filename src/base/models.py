from __future__ import unicode_literals

from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=144, blank=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Posición")
        verbose_name_plural = _("Posiciones")


class Pages(models.Model):
    name = models.CharField(max_length=144, blank=True)
    description = RichTextField(blank=True)
    have_icon = models.BooleanField(default=False)
    url = models.CharField(max_length=18, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Página")
        verbose_name_plural = _("Paginas")


class Carousel(models.Model):
    name = models.CharField(max_length=144, blank=True)
    description = RichTextField(blank=True)
    page = models.ForeignKey(Pages, default=1, on_delete=models.CASCADE,blank=True)
    Position = models.ForeignKey(Position, default=1, on_delete=models.CASCADE,blank=True)
    crated_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Carousel")
        verbose_name_plural = _("Carousel")

class CarouselImage(models.Model):
    Carousel = models.ForeignKey(Carousel, related_name='images', on_delete=models.CASCADE,)
    image = models.ImageField(upload_to="frontend/")
    name = models.CharField(max_length=144, blank=True)
    text = RichTextField(blank=True)
    call_to_action_url = models.ForeignKey(FlatPage, on_delete=models.CASCADE, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now=True,)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Imágen del carousel")
        verbose_name_plural = _("Imagenes del carousel")


class Widget(models.Model):
    name = models.CharField(max_length=144, blank=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Widget")
        verbose_name_plural = _("Widgets")


class Site(models.Model):
    name = models.CharField(max_length = 140, blank=True)
    title = models.CharField(max_length=144, blank=True, null=True)
    description = RichTextField( blank=True)
    short_description = RichTextField( blank=True)
    url = models.CharField(max_length = 140, blank=True)
    phone = models.CharField(max_length=144, blank=True, null=True)
    email = models.CharField(max_length=144, blank=True, null=True)
    logo = models.ImageField(upload_to='site/', default='/static/base/img/moby.png')
    site_img = models.ImageField(upload_to='site/', default='/static/base/img/moby.png')
    services_img = models.ImageField(upload_to='site/', default='/static/base/img/moby.png')
    products_img = models.ImageField(upload_to='site/', default='/static/base/img/moby.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Informacion del sitio')
        verbose_name_plural = _('Informacion del sitio')


class SocialMedia(models.Model):
    site = models.ForeignKey(Site, related_name='Social_Media', on_delete=models.CASCADE,)
    url = models.CharField(max_length = 1444, blank=True)
    name = models.CharField(max_length = 1444, blank=True)
    icon = models.CharField(max_length = 1444, blank=True)
    title = models.CharField(max_length = 1444, blank=True)