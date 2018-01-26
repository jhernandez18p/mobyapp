from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import (
    Position,
    Pages,
    Carousel,
    CarouselImage,
    Widget,
)

class CarouselImageInline(admin.StackedInline):
    model = CarouselImage
    extra = 1

class CarouselAdmin(admin.ModelAdmin):
    inlines = [CarouselImageInline,]

admin.site.register(Position)
admin.site.register(Pages)
admin.site.register(Widget)
admin.site.register(CarouselImage)
admin.site.register(Carousel, CarouselAdmin)
