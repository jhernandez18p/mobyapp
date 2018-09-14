from __future__ import unicode_literals

import os
import random

from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField
# from src.utils.libs import (upload_location)

def get_img(isinstance):

    url = 'sales/arts/base.jpg'

    return url

def get_upload_path(instance, filename):
    _filename = filename.split('.')
    _filename_ext = _filename[-1]
    _filename_name = ''.join(random.choice(_filename[0]) for _ in range(5))
    filename = '%s.%s' % (_filename_name,_filename_ext)
    print(filename)
    try:
        a = instance.__class__.__name__
        print(instance.__class__.objects.all())
    except:
        a = 'frontend'
    return os.path.join('sales/%s/'%(a.lower()), datetime.now().date().strftime("%Y/%m/%d"), filename)

def get_art_upload_path(instance, filename):
    if filename:
        _filename = filename.split('.')
        _filename_ext = _filename[-1]
        _filename_name = ''.join(random.choice(_filename[0]) for _ in range(5))
        filename = '%s.%s' % (_filename_name,_filename_ext)
        print(filename)
    else:
        filename = instance.code + '.jpg'
    try:
        a = instance.__class__.__name__
        print(instance.__class__.objects.all())
    except:
        a = 'frontend'
    return os.path.join('sales/arts/', filename)

def create_slug(instance, new_slug=None):

    if instance.__class__.__name__ == 'Article':
        name = instance.description
        try:
            name = name.split('<p>')
            name = name[1].split('<')
            name = name[0]
        except:
            pass
        slug = slugify(name)
    else:
        slug = slugify(instance.code)
            

    if new_slug is not None:
        slug = new_slug
    
    qs = instance.__class__.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    # else:
    #     new_slug = "%s-%s" %(instance.__class__, instance.id)
    #     return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.name == None:
        instance.name = instance.code

def pre_save_receiver_with_slug(sender, instance, *args, **kwargs):

    if not instance.slug:
        instance.slug = create_slug(instance)

def art_pre_save_receiver(sender, instance, *args, **kwargs):

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
    img = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Imágen'))
    name = models.CharField(max_length=256, blank=True, verbose_name=_('Nombre'))
    code = models.CharField(max_length=256, blank=True, verbose_name=_('Código'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('Linea')
        verbose_name_plural = _('Lineas')


class SubLine(models.Model): 
    # Business logic art. key 
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    img = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Imágen'))
    name = models.CharField(max_length=256, blank=True, verbose_name=_('Nombre'))
    code = models.CharField(max_length=256, blank=True, verbose_name=_('Código'))
    parent = models.ForeignKey(Line, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('Linea padre'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('Sub linea')
        verbose_name_plural = _('Sub Lineas')


class Color(models.Model):
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    hex_code = models.CharField(max_length=9, blank=True, verbose_name=_('Código Hexadecimal'))
    name = models.CharField(max_length=256, blank=True, verbose_name=_('Nombre'))
    code = models.CharField(max_length=256, blank=True, verbose_name=_('Código'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colores')


class Type(models.Model): 
    # For web use
    background = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Foto de fondo'))
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    img = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Imágen'))
    name = models.CharField(max_length=256, blank=True, verbose_name=_('Nombre'))
    code = models.CharField(max_length=256, blank=True, verbose_name=_('Código'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('Tipo de artículo')
        verbose_name_plural = _('Tipos de artículos')


class Provider(models.Model):
    background = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Foto de fondo'))
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    img = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Imágen'))
    logo = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Logo'))
    name = models.CharField(max_length=256, blank=True, verbose_name=_('Nombre'))
    slug = models.CharField(max_length=256, blank=True, verbose_name=_('Slug \"SEO\"'))
    website = models.CharField(max_length=256, blank=True, verbose_name=_('Dirección url'))
    code = models.CharField(max_length=256, blank=True, verbose_name=_('Código'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('Proveedor')
        verbose_name_plural = _('Proveedores')

    # def get_absolute_url(self):
        # return reverse('sales:provider_detail', kwargs={'slug': self.slug})


class Brands(models.Model):
    background = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Foto de fondo'))
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    img = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Imágen'))
    logo = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Logo'))
    name = models.CharField(max_length=256, blank=True, verbose_name=_('Nombre'))
    slug = models.CharField(max_length=256, blank=True, verbose_name=_('Slug \"SEO\"'))
    website = models.CharField(max_length=256, blank=True, verbose_name=_('Dirección url'))
    code = models.CharField(max_length=256, blank=True, verbose_name=_('Código'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('Marca')
        verbose_name_plural = _('Marcas')

    def get_absolute_url(self):
        return reverse('sales:brand_detail', kwargs={'slug': self.slug})


class Department(models.Model): 
    # Only for web use
    background = models.ImageField(upload_to=get_upload_path, blank=True, null=True, verbose_name=_('Foto de fondo'))
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    img = models.ImageField(upload_to=get_upload_path, blank=True, null=True, verbose_name=_('Imágen'))
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('Nombre'))
    slug = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('Slug \"SEO\"'))
    code = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('Código'))
    order = models.IntegerField(blank=True, null=True, verbose_name=_('Orden'), default=1)

    def __str__(self):
        return self.name

    def save(self):
        if self.order == 1:
            self.order = self.id
        super(Department, self).save()

    class Meta:
        ordering = ['order']
        verbose_name = _('Departamento')
        verbose_name_plural = _('Departamentos')


    def get_absolute_url(self):
        return reverse('sales:department_detail', kwargs={'slug': self.slug})


class Category(models.Model):
    # Business Logic art. cat.
    background = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name=_('Foto de fondo'))
    description = RichTextField(blank=True, verbose_name=_('Descripción'))
    img = models.ImageField(max_length=256, blank=True, verbose_name=_('Imágen'))
    name = models.CharField(max_length=256, blank=True, verbose_name=_('Nombre'))
    parent = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('Categoría padre'))
    slug = models.CharField(max_length=256, blank=True, verbose_name=_('Slug \"SEO\"'))
    code = models.CharField(max_length=256, blank=True, verbose_name=_('Código'))
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def get_absolute_url(self):
        return reverse('sales:category_detail', kwargs={'slug': self.name.lower()})


class Article(models.Model):

    code = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_('Código de articulo')
    )
    model = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_('Modelo')
    )
    name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_('Nombre')
    )
    origin = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_('Origen')
    )
    sales_unit = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_('Unidad de ventas')
    )
    ref = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_('Referencia')
    ) #   
    description = RichTextField(blank=True, verbose_name=_('Descripción'), max_length=2000)
    item_type = models.ForeignKey(
        Type,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_('Tipo de articulo'),
    )
    line = models.ForeignKey(
        Line,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_('Linea')
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_('Categoría')
    )
    color = models.ForeignKey(
        Color,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_('Color')
    )
    department = models.ForeignKey(
        Department,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_('Departamento')
    )
    brand = models.ForeignKey(
        Brands,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_('Marca'),
    )
    provider = models.ForeignKey(
        Provider,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_('Proveedor')
    )
    sub_line = models.ForeignKey(
        SubLine,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_('Sublinea')
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
        max_length=500,
        verbose_name=_('URL \"SEO\"')
    )
    stock = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        verbose_name=_('Stock')
    )
    views = models.SmallIntegerField(
        default=0,
        blank=True,
        verbose_name=_('Numero de visitas')
    )
    picture = models.ImageField(
        blank=True,
        null=True,
        upload_to=get_upload_path,
        verbose_name=_('Foto de articulo')
    )
    price_1 = models.DecimalField(
        decimal_places=2,
        max_digits=99,
        blank=True,
        null=True,
        verbose_name=_('Precio 1')
    )
    price_2 = models.DecimalField(
        decimal_places=2,
        max_digits=99,
        blank=True,
        null=True,
        verbose_name=_('Precio 2')
    )
    price_3 = models.DecimalField(
        decimal_places=2,
        max_digits=99,
        blank=True,
        null=True,
        verbose_name=_('Precio 3')
    )
    price_4 = models.DecimalField(
        decimal_places=2,
        max_digits=99,
        blank=True,
        null=True,
        verbose_name=_('Precio 4')
    )
    price_5 = models.DecimalField(
        decimal_places=2,
        max_digits=99,
        blank=True,
        null=True,
        verbose_name=_('Precio 5')
    )
    updated = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name=_('Ultima actualización')
    )
    created_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name=_('Creado')
    )
    img = models.ImageField( 
        upload_to=get_art_upload_path,#"sales/arts/",
        blank=True, 
        null=True, 
        verbose_name=_('Imagen de articulo'), 
        default='sales/arts/base.jpg'
    )
    active = models.BooleanField(
        default=False,
        verbose_name=_('Activo')
    )
    featured = models.BooleanField(
        default=False,
        verbose_name=_('Destacado')
    )
    imported = models.BooleanField(
        default=False,
        verbose_name=_('Importado')
    )
    is_shipping_required = models.BooleanField(
        default=False,
        verbose_name=_('Requiere envio')
    )

    # def __str__(self):
    #     return self.code

    def get_absolute_url(self):
        return reverse('sales:product_detail', kwargs={'slug': self.slug})

    def counter(self):
        return len(self.objects.all())
    
    class Meta:
        ordering = ["-featured", "code"]
        verbose_name = _('Producto')
        verbose_name_plural = _('Productos')


pre_save.connect(art_pre_save_receiver, sender=Article)
pre_save.connect(pre_save_receiver, sender=Line)
pre_save.connect(pre_save_receiver, sender=SubLine)
pre_save.connect(pre_save_receiver, sender=Color)
pre_save.connect(pre_save_receiver, sender=Type)
pre_save.connect(pre_save_receiver, sender=Provider)
pre_save.connect(pre_save_receiver_with_slug, sender=Category)
pre_save.connect(pre_save_receiver_with_slug, sender=Department)
pre_save.connect(pre_save_receiver_with_slug, sender=Brands)