from django.contrib import admin
from .models import (Comment, Post)
# Register your models here.


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['author',]

    class Meta:
        model = Comment

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "created_at"]
    list_display_links = ["created_at",]
    list_editable = ["title"]
    list_filter = ["created_at", "updated"]
    search_fields = ["title", "content"]
    
    class Meta:
        model = Post


admin.site.register(Comment, CommentModelAdmin)
admin.site.register(Post, PostModelAdmin)