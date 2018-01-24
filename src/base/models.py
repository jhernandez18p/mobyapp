from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=144, blank=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name


class Pages(models.Model):
    name = models.CharField(max_length=144, blank=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name


class Widget(models.Model):
    name = models.CharField(max_length=144, blank=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name


class Carousel(models.Model):
    name = models.CharField(max_length=144, blank=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name


