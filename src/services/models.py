from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=140, blank=True)
    content = RichTextField(blank=True)
    slug = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return self.name