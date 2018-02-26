from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import (
    Line,
    SubLine,
    Type,
    Color,
    Provider,
    Department,
    Category,
    Article,
)
from src.ventas.resources import ArticleResource
# Register your models here.

admin.site.register(Line)
admin.site.register(SubLine)
admin.site.register(Type)
admin.site.register(Color)
admin.site.register(Provider)
admin.site.register(Department)
admin.site.register(Category)


class ArticleAdmin(ImportExportModelAdmin):
    resource_class = ArticleResource


admin.site.register(Article, ArticleAdmin)