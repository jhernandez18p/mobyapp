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
# Register your models here.

admin.site.register(Line)
admin.site.register(SubLine)
admin.site.register(Type)
admin.site.register(Color)
admin.site.register(Provider)
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(Article)
