from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _


class ApiConfig(AppConfig):
    name = 'src.api'
    verbose_name = _("Api")