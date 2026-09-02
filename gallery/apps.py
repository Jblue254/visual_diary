from django.apps import AppConfig
from django.apps import AppConfig


class GalleryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gallery'

    def ready(self):
        import gallery.signals


class GalleryConfig(AppConfig):
    name = 'gallery'
