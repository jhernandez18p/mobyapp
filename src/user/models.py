from __future__ import unicode_literals

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
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class Frecuency(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE,)
    average = models.CharField(max_length=144, blank=True)
    monday = models.CharField(max_length=144, blank=True)
    tuesday = models.CharField(max_length=144, blank=True)
    wednesday = models.CharField(max_length=144, blank=True)
    thursday = models.CharField(max_length=144, blank=True)
    friday = models.CharField(max_length=144, blank=True)
    saturday = models.CharField(max_length=144, blank=True)
    sunday = models.CharField(max_length=144, blank=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Frecuencia de visita'
        verbose_name_plural = 'Frecuencia de visitas'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=144, blank=True)
    bio = RichTextField( blank=True)
    description = RichTextField( blank=True)
    member_since = models.CharField(max_length=144, blank=True)
    direction1 = RichTextField( blank=True)
    direction2 = RichTextField( blank=True)
    phone = models.CharField(max_length=144, blank=True)
    is_active = models.CharField(max_length=144, blank=True)
    respons = models.CharField(max_length=144, blank=True)
    country = models.CharField(max_length=144, blank=True) 
    city = models.CharField(max_length=144, blank=True)
    zip_code = RichTextField( blank=True)
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=True)
    is_provider = models.BooleanField(default=False)
    seller = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE,)
    seller_description = RichTextField( blank=True)
    score = models.CharField(max_length=144, blank=True)
    saldo = models.CharField(max_length=144, blank=True)
    max_credit = models.CharField(max_length=144, blank=True)
    payment_lapse = models.CharField(max_length=144, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfiles de usuarios'