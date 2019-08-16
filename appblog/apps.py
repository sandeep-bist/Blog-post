from django.apps import AppConfig


class AppblogConfig(AppConfig):
    name = 'appblog'

    def ready(self):
        import appblog.signals