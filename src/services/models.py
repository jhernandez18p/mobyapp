from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField

class Service(models.Model):
    name = models.CharField(max_length=140, blank=True)
    title = models.CharField(max_length=140, blank=True)
    content = RichTextField(blank=True)
    slug = models.CharField(max_length=140, blank=True)
    image = models.ImageField(upload_to="service/", blank=True)
    background = models.ImageField(upload_to="service/", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Servicio')
        verbose_name_plural = _('Servicios')

    def get_absolute_url(self):
        return reverse("services:detail", kwargs={"slug": self.slug})


class ServiceImage(models.Model):
    Service = models.ForeignKey(Service, related_name='images', on_delete=models.CASCADE,)
    image = models.ImageField(upload_to="service/", blank=True)
    name = models.CharField(max_length=144, blank=True)
    text = RichTextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now=True,)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Imágen del carousel")
        verbose_name_plural = _("Imagenes del carousel")


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Service.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_service_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_service_receiver, sender=Service)