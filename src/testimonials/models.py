from __future__ import unicode_literals
from django.db import models

from ckeditor.fields import RichTextField
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Testimonial(models.Model):
    """
    """
    name = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE,verbose_name=_('Autor del testimonio'))
    company = models.CharField(max_length=120,verbose_name=_('Empresa'))
    description = RichTextField()
    img = models.ImageField(verbose_name=_('Imágen de testimonio'),
        upload_to='testimonials/', 
        null=True, 
        blank=True, 
        default='',
    )

    def __str__(self):
        return self.company