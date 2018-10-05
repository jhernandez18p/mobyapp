from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from datetime import datetime
import os

from ckeditor.fields import RichTextField

def get_upload_path(instance, filename):
    try:
        a = instance.__class__.__name__
        print(instance.__class__.objects.all())
    except:
        a = 'frontend'
    return os.path.join('sales/%s/'%(a.lower()), datetime.now().date().strftime("%Y/%m/%d"), filename)

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = instance.__class__.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


class Service(models.Model):
    name = models.CharField(max_length=140, blank=True, verbose_name=_('Nombre'))
    title = models.CharField(max_length=140, blank=True, verbose_name=_('Título'))
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    content = RichTextField(blank=True, verbose_name=_('Contenido'))
    slug = models.CharField(max_length=140, blank=True, verbose_name=_('Slug \"SEO\"'))
    image = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Imágen'))
    featured = models.BooleanField(
        default=False,
        verbose_name=_('Servicio destacado')
    )
    position = models.PositiveIntegerField(verbose_name=_('Posición'), blank=True, null=True)
    background = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Foto de fondo'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Servicio')
        verbose_name_plural = _('Servicios')

    def get_absolute_url(self):
        return reverse("services:detail", kwargs={"slug": self.slug})


class ServiceImage(models.Model):
    Service = models.ForeignKey(Service, related_name='images', on_delete=models.CASCADE,)
    image = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Imágen'))
    name = models.CharField(max_length=144, blank=True, verbose_name=_('Nombre'))
    text = RichTextField(blank=True, verbose_name=_('Descripción'))
    uploaded_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Imágen del carousel")
        verbose_name_plural = _("Imagenes del carousel")


pre_save.connect(pre_save_receiver, sender=Service)