from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['company',]

    class Meta:
        model = Testimonial

admin.site.register(Testimonial, TestimonialAdmin)