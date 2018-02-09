from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _


class GalleryConfig(AppConfig):
    name = 'src.gallery'
    verbose_name = _("Modulo Multimedia")