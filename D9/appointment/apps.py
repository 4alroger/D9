from django.apps import AppConfig


class AppointmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointment'

    # переопределяем метод ready для дальнейшего импорта
    def ready(self):
        from .signals import notify_managers_appointment

