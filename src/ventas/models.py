from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from datetime import datetime
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
import os

from src.utils.libs import (upload_location)

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


class Photo(models.Model):
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    file = models.FileField(upload_to=get_upload_path, blank=True, verbose_name=_('Foto'))
    name = models.CharField(max_length=255, blank=True, verbose_name=_('Nombre'))
    title = models.CharField(max_length=255, blank=True, verbose_name=_('Título'))
    uploaded = models.DateTimeField(auto_now_add=True, verbose_name=_('¿Cuando fue cargado?'))

    def __srt__(self):
        return self.name

    class Meta:
        verbose_name = _('Foto')
        verbose_name_plural = _('Fotos')


class Line(models.Model): 
    # Business logic art. key 
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    img = ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Imágen'))
    name = models.CharField(max_length=144, blank=True, verbose_name=_('Nombre'))
    code = models.CharField(max_length=144, blank=True, verbose_name=_('Código'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Linea')
        verbose_name_plural = _('Lineas')


class SubLine(models.Model): 
    # Business logic art. key 
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    img = ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Imágen'))
    name = models.CharField(max_length=144, blank=True, verbose_name=_('Nombre'))
    code = models.CharField(max_length=144, blank=True, verbose_name=_('Código'))
    parent = models.ForeignKey(Line, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('Linea padre'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Sublinea')
        verbose_name_plural = _('SubLineas')


class Color(models.Model):
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    hex_code = models.CharField(max_length=9, blank=True, verbose_name=_('Código Hexadecimal'))
    name = models.CharField(max_length=144, blank=True, verbose_name=_('Nombre'))
    code = models.CharField(max_length=144, blank=True, verbose_name=_('Código'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colores')


class Type(models.Model): 
    # For web use
    background = ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Foto de fondo'))
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    img = ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Imágen'))
    name = models.CharField(max_length=144, blank=True, verbose_name=_('Nombre'))
    code = models.CharField(max_length=144, blank=True, verbose_name=_('Código'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tipo de artículo')
        verbose_name_plural = _('Tipos de artículos')


class Provider(models.Model):
    background = ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Foto de fondo'))
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    img = ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Imágen'))
    logo = ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Logo'))
    name = models.CharField(max_length=144, blank=True, verbose_name=_('Nombre'))
    slug = models.CharField(max_length=144, blank=True, verbose_name=_('Slug \"SEO\"'))
    website = models.CharField(max_length=144, blank=True, verbose_name=_('Dirección url'))
    code = models.CharField(max_length=144, blank=True, verbose_name=_('Código'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Proveedor')
        verbose_name_plural = _('Proveedores')

    # def get_absolute_url(self):
        # return reverse('sales:provider_detail', kwargs={'slug': self.slug})


class Brands(models.Model):
    background = ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Foto de fondo'))
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    img = ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Imágen'))
    logo = ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Logo'))
    name = models.CharField(max_length=144, blank=True, verbose_name=_('Nombre'))
    slug = models.CharField(max_length=144, blank=True, verbose_name=_('Slug \"SEO\"'))
    website = models.CharField(max_length=144, blank=True, verbose_name=_('Dirección url'))
    code = models.CharField(max_length=144, blank=True, verbose_name=_('Código'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Marca')
        verbose_name_plural = _('Marcas')

    def get_absolute_url(self):
        return reverse('sales:brand_detail', kwargs={'slug': self.slug})


class Department(models.Model): 
    # Only for web use
    background = ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Foto de fondo'))
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    img = ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Imágen'))
    name = models.CharField(max_length=144, blank=True, verbose_name=_('Nombre'))
    slug = models.CharField(max_length=144, blank=True, verbose_name=_('Slug \"SEO\"'))
    code = models.CharField(max_length=144, blank=True, verbose_name=_('Código'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Departamento')
        verbose_name_plural = _('Departamentos')


    def get_absolute_url(self):
        return reverse('sales:department_detail', kwargs={'slug': self.name.lower()})


class Category(models.Model):
    # Business Logic art. cat.
    background = ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Foto de fondo'))
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    img = ImageField(max_length=144, blank=True, verbose_name=_('Imágen'))
    name = models.CharField(max_length=144, blank=True, verbose_name=_('Nombre'))
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('Categoría padre'))
    slug = models.CharField(max_length=144, blank=True, verbose_name=_('Slug \"SEO\"'))
    code = models.CharField(max_length=144, blank=True, verbose_name=_('Código'))
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def get_absolute_url(self):
        return reverse('sales:category_detail', kwargs={'slug': self.name.lower()})


class Article(models.Model):
    # bo_category = models.CharField(blank=True, max_length=144, verbose_name=_('Categoría \"se importación\"'))
    # bo_color = models.CharField(blank=True, max_length=144, verbose_name=_('Color \"se importación\"'))
    # bo_department = models.CharField(blank=True, max_length=144, verbose_name=_('Departamento \"se importación\"'))
    # bo_item_type = models.CharField(blank=True, max_length=144, verbose_name=_('Tipo de articulo \"se importación\"'))
    # bo_line = models.CharField(blank=True, max_length=144, verbose_name=_('Linea \"se importación\"'))
    # bo_provider = models.CharField(blank=True, max_length=144, verbose_name=_('Proveedor \"se importación\"'))
    # bo_sub_line = models.CharField(blank=True, max_length=144, verbose_name=_('Sublinea \"se importación\"'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name=_('Categoría'))
    code = models.CharField(max_length=144, blank=True, verbose_name=_('Código de articulo'))
    color = models.ForeignKey(Color, on_delete=models.CASCADE,verbose_name=_('Color'))
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name=_('Creado'))
    department = models.ForeignKey(Department, on_delete=models.CASCADE,verbose_name=_('Departamento'))
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    img = models.CharField(max_length=144, blank=True, verbose_name=_('Imagen de articulo'))
    imported = models.BooleanField(default=False, verbose_name=_('Importado'))
    is_shipping_required = models.BooleanField(default=False, verbose_name=_('Requiere envio'))
    item_type = models.ForeignKey(Type, on_delete=models.CASCADE,verbose_name=_('Tipo de articulo'))
    line = models.ForeignKey(Line, on_delete=models.CASCADE,verbose_name=_('Linea'))
    model = models.CharField(max_length=144, blank=True, verbose_name=_('Modelo'))
    name = models.CharField(max_length=144, blank=False, verbose_name=_('Nombre'))
    origin = models.CharField(max_length=144, blank=True, verbose_name=_('Origen'))
    picture = ImageField(blank=True, upload_to=get_upload_path, verbose_name=_('Foto de articulo'))
    price_1 = models.DecimalField(decimal_places=2, max_digits=99, blank=True, null=True, verbose_name=_('Precio 1'))
    price_2 = models.DecimalField(decimal_places=2, max_digits=99, blank=True, null=True, verbose_name=_('Precio 2'))
    price_3 = models.DecimalField(decimal_places=2, max_digits=99, blank=True, null=True, verbose_name=_('Precio 3'))
    price_4 = models.DecimalField(decimal_places=2, max_digits=99, blank=True, null=True, verbose_name=_('Precio 4'))
    price_5 = models.DecimalField(decimal_places=2, max_digits=99, blank=True, null=True, verbose_name=_('Precio 5'))
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,verbose_name=_('Proveedor'))
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE,null=True,verbose_name=_('Marca'))
    ref = models.CharField(max_length=144, blank=True, verbose_name=_('Referencia')) # 
    sales_unit = models.CharField(max_length=144, blank=True, verbose_name=_('Unidad de ventas'))
    slug = models.SlugField(unique=True, blank=True, verbose_name=_('URL \"SEO\"'))
    stock = models.IntegerField(default=0, blank=True, verbose_name=_('Stock'))
    sub_line = models.ForeignKey(SubLine, on_delete=models.CASCADE,verbose_name=_('Sublinea'))
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name=_('Ultima actualización'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at", "-updated"]
        verbose_name = _('Artículo')
        verbose_name_plural = _('Artículos')

    def get_absolute_url(self):
        return reverse('sales:product_detail', kwargs={'slug': self.slug})

pre_save.connect(pre_save_receiver, sender=Article)
pre_save.connect(pre_save_receiver, sender=Category)
pre_save.connect(pre_save_receiver, sender=Department)
pre_save.connect(pre_save_receiver, sender=Brands)
pre_save.connect(pre_save_receiver, sender=Provider)