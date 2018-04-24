from __future__ import unicode_literals
from ckeditor.fields import RichTextField
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
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField
from datetime import datetime
from django.db.models import Q
import os

from src.utils.libs import (upload_location)

def get_upload_path(instance, filename):
    try:
        a = instance.__class__.__name__
        print(instance.__class__.objects.all())
    except:
        a = 'frontend'
    return os.path.join('blog/%s/'%(a.lower()), datetime.now().date().strftime("%Y/%m/%d"), filename)

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = instance.__class__.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    if not instance.updated_by:
        instance.updated_by = instance.author

class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return super(PostManager, self).filter(draft=False).filter(published__lte=timezone.now())


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE,verbose_name=_('Autor del post'))
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE,verbose_name=_('Actualizado por'), blank=True)
    title = models.CharField(max_length=120,verbose_name=_('Titulo del post'))
    sub_title = models.CharField(max_length=120, blank=True,verbose_name=_('Subtitulo'))
    text = RichTextField(verbose_name="Contenido del post")
    is_public = models.BooleanField(default=False,verbose_name=_('¿Es público?'))
    draft = models.BooleanField(default=True,verbose_name=_('¿Es borrador?'))
    published = models.DateField(auto_now=True, auto_now_add=False,verbose_name=_('Fecha de publicación'))
    read_time =  models.IntegerField(null=True, blank=True, verbose_name='Tiempo de lectura (Minutos)') #assume minutes
    updated = models.DateTimeField(auto_now=True, auto_now_add=False,verbose_name=_('Ultima actualización'))
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True,verbose_name=_('Fecha de creación'))
    img = models.ImageField(verbose_name=_('Imágen de portada'),
        upload_to=get_upload_path, 
        null=True, 
        blank=True, 
        default='',
    )
    background = models.ImageField(verbose_name=_('Imágen de fondo'),
        upload_to=get_upload_path,
        null=True, 
        blank=True, 
        default='',
    )
    slug = models.SlugField(unique=True, blank=True,verbose_name=_('Nombre url SEO'))

    objects = PostManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"slug": self.slug})

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    class Meta:
        ordering = ["created_at"]
        verbose_name = 'Articulo del blog'
        verbose_name_plural = 'Articulos del blog'


class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id= obj_id).filter(parent=None)
        return qs


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE,verbose_name=_('Autor del comentario'))
    content = RichTextField(verbose_name=_('Comentario'))
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE,verbose_name=_('Comentario padre'))
    approved = models.BooleanField(verbose_name=_('¿Está aprovado?'), default=True)
    timestamp = models.DateTimeField(auto_now_add=True,verbose_name=_('Tiempo creado'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True,verbose_name=_('Post asociado'))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,verbose_name=_('Tipo de contenido'))
    content_object = GenericForeignKey('content_type', 'object_id')
    object_id = models.PositiveIntegerField(verbose_name=_('Id de relación'))

    objects = CommentManager()

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return str(self.author)

    def get_absolute_url(self):
        return reverse("comments:thread", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("comments:delete", kwargs={"id": self.id})
        
    def children(self): #replies
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True


#Post.objects.all()
#Post.objects.create(user=user, title="Some time")
pre_save.connect(pre_save_post_receiver, sender=Post)