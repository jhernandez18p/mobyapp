from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Line, SubLine, Type, Color, Provider, Department,\
    Category, Article, Brands 

from src.ventas.resources import ArticleResource, LineResource,\
    SubLineResource, TypeResource, ColorResource, ProviderResource,\
    DepartmentResource, CategoryResource, BrandsResource


class LineAdmin(ImportExportModelAdmin):
    list_display = [
        'id','code','name'
    ]
    list_display_links = [
        'id'
    ]
    list_editable = [
        'name'
    ]
    list_filter = [
        'name'
    ]
    search_fields = [
        'name'
    ]
    resource_class = LineResource


class SubLineAdmin(ImportExportModelAdmin):
    list_display = [
        'code','name','parent'
    ]
    list_display_links = [
        'code'
    ]
    list_editable = [
        'name','parent'
    ]
    list_filter = [
        'parent'
    ]
    search_fields = [
        'name','parent'
    ]
    resource_class = SubLineResource


class TypeAdmin(ImportExportModelAdmin):
    list_display = [
        'code','name'
    ]
    list_display_links = [
        'code'
    ]
    list_editable = [
        'name'
    ]
    list_filter = [
        'name'
    ]
    search_fields = [
        'name'
    ]
    resource_class = TypeResource


class ColorAdmin(ImportExportModelAdmin):
    list_display = [
        'code','name'
    ]
    list_display_links = [
        'code'
    ]
    list_editable = [
        'name'
    ]
    list_filter = [
        'name'
    ]
    search_fields = [
        'name'
    ]
    resource_class = ColorResource


class ProviderAdmin(ImportExportModelAdmin):
    list_display = [
        'id','code','name'
    ]
    list_display_links = [
        'id'
    ]
    list_editable = [
        'name'
    ]
    list_filter = [
        'name'
    ]
    search_fields = [
        'name'
    ]
    resource_class = ProviderResource


class BrandsAdmin(ImportExportModelAdmin):
    list_display = [
        'id','name','logo'
    ]
    list_display_links = [
        'id'
    ]
    list_editable = [
        'name','logo'
    ]
    list_filter = [
        'name'
    ]
    search_fields = [
        'name'
    ]
    resource_class = BrandsResource


class DepartmentAdmin(ImportExportModelAdmin):
    list_display = [
        'name','order'
    ]
    list_display_links = [
        'name'
    ]
    list_editable = [
        'order'
    ]
    list_filter = [
        'name'
    ]
    search_fields = [
        'name'
    ]
    resource_class = DepartmentResource


class CategoryAdmin(ImportExportModelAdmin):
    list_display = [
        'code','name','parent'
    ]
    list_display_links = [
        'code'
    ]
    list_editable = [
        'name','parent'
    ]
    list_filter = [
        'parent'
    ]
    search_fields = [
        'name','parent'
    ]
    resource_class = CategoryResource


class ArticleAdmin(ImportExportModelAdmin):
    list_display = [
        'code',
        'line',
        'category',
        'sub_line',
        'color',
        'provider',
    ]
    list_display_links = [
        'code',
    ]
    list_editable = [
        'provider',
        'line',
        'category',
        'sub_line',
        'color',
    ]
    list_filter = [
        'department',
    ]
    search_fields = [
        'code',
    ]
    resource_class = ArticleResource


admin.site.register(Article, ArticleAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(SubLine, SubLineAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Category, CategoryAdmin)