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
    Brands,
)
from src.ventas.resources import ArticleResource, LineResource,\
    SubLineResource, TypeResource, ColorResource, ProviderResource,\
    DepartmentResource, CategoryResource, BrandsResource



class LineAdmin(ImportExportModelAdmin):
    resource_class = LineResource


class SubLineAdmin(ImportExportModelAdmin):
    resource_class = SubLineResource


class TypeAdmin(ImportExportModelAdmin):
    resource_class = TypeResource


class ColorAdmin(ImportExportModelAdmin):
    resource_class = ColorResource


class ProviderAdmin(ImportExportModelAdmin):
    resource_class = ProviderResource


class BrandsAdmin(ImportExportModelAdmin):
    resource_class = BrandsResource


class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource


class ArticleAdmin(ImportExportModelAdmin):
    resource_class = ArticleResource


admin.site.register(Article, ArticleAdmin)
admin.site.register(Line,LineAdmin)
admin.site.register(SubLine,SubLineAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Provider,ProviderAdmin)
admin.site.register(Brands,BrandsAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Category,CategoryAdmin)