from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=144, blank=True, verbose_name='Pregunta')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    text = RichTextField(blank=True)
    
    def __str__(self):
        return self.question.title

    class Meta:
        ordering = ['question']