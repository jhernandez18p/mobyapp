from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(), label="Comentario")

    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content':'Comentario',
        }

