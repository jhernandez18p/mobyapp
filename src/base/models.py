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
        verbose_name_plural = _("Carouseles")

class CarouselImage(models.Model):
    Carousel = models.ForeignKey(Carousel, related_name='images', on_delete=models.CASCADE,)
    image = models.ImageField(upload_to="frontend/")
    name = models.CharField(max_length=144, blank=True)
    text = RichTextField(blank=True)
    call_to_action_url = models.ForeignKey(FlatPage, on_delete=models.CASCADE, blank=True)
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
