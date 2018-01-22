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


from ckeditor.fields import RichTextField

from src.utils.libs import (upload_location,get_read_time,count_words)


class Line(models.Model): # Business logic art. key 
    name = models.CharField(max_length=144, blank=True)
    description = RichTextField(blank=True)
    img = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Linea'
        verbose_name_plural = 'Lineas'


class SubLine(models.Model): # Business logic art. key 
    name = models.CharField(max_length=144, blank=True)
    parent = models.ForeignKey(Line, null=True, blank=True, on_delete=models.CASCADE,)
    description = RichTextField(blank=True)
    img = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sub-linea'
        verbose_name_plural = 'Sub-Linea'


class Color(models.Model):
    name = models.CharField(max_length=144, blank=True)
    hex_code = models.CharField(max_length=9, blank=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'


class Type(models.Model): # For web use
    name = models.CharField(max_length=144, blank=True)
    description = RichTextField(blank=True)
    img = models.ImageField(upload_to='', blank=True)
    background = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de artículo'
        verbose_name_plural = 'Tipos de artículos'


class Provider(models.Model):
    name = models.CharField(max_length=144, blank=True)
    description = RichTextField(blank=True)
    img = models.ImageField(upload_to='', blank=True)
    logo = models.ImageField(upload_to='', blank=True)
    background = models.ImageField(upload_to='', blank=True)
    website = models.CharField(max_length=144, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class Department(models.Model): # For web use
    name = models.CharField(max_length=144, blank=True)
    description = RichTextField(blank=True)
    img = models.ImageField(upload_to='', blank=True)
    background = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría web'
        verbose_name_plural = 'Categorías web'


class Category(models.Model): # Business Logic art. cat.
    name = models.CharField(max_length=144, blank=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE,)
    description = RichTextField(blank=True)
    img = models.ImageField(max_length=144, blank=True)
    background = models.ImageField(upload_to='', blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class Article(models.Model):
    name = models.CharField(max_length=144, blank=True)
    description = RichTextField(blank=True)
    code = models.CharField(max_length=144, blank=True)
    ref = models.CharField(max_length=144, blank=True) # 
    line = models.ForeignKey(Line, blank=True, on_delete=models.CASCADE,)
    sub_line = models.ForeignKey(SubLine, blank=True, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE,)
    provider = models.ForeignKey(Provider, blank=True, on_delete=models.CASCADE,)
    color = models.ForeignKey(Color, blank=True, on_delete=models.CASCADE,)
    department = models.ForeignKey(Department, blank=True, on_delete=models.CASCADE,)
    model = models.CharField(max_length=144, blank=True)
    origin = models.CharField(max_length=144, blank=True)
    sales_unit = models.CharField(max_length=144, blank=True)
    stock = models.IntegerField(default=0, blank=True)
    price_1 = models.DecimalField(decimal_places=2, max_digits=99, blank=True)
    price_2 = models.DecimalField(decimal_places=2, max_digits=99, blank=True)
    price_3 = models.DecimalField(decimal_places=2, max_digits=99, blank=True)
    price_4 = models.DecimalField(decimal_places=2, max_digits=99, blank=True)
    price_5 = models.DecimalField(decimal_places=2, max_digits=99, blank=True)
    item_type = models.ForeignKey(Type, blank=True, on_delete=models.CASCADE,)
    is_shipping_required = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    picture = models.ImageField(blank=True, upload_to='')
    img = models.ImageField(blank=True, upload_to='')

    def __srt__(self):
        return self.name

    class Meta:
        ordering = ["-created_at", "-updated"]
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Article.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_article_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_article_receiver, sender=Article)