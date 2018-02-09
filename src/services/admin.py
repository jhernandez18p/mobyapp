from django.contrib import admin

# Register your models here.
from .models import (
    Service,
    ServiceImage
)

class ServiceInline(admin.StackedInline):
    model = ServiceImage
    extra = 3


class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['name',]
    inlines = [ServiceInline,]

    class Meta:
        model = Service



admin.site.register(Service, ServiceModelAdmin)