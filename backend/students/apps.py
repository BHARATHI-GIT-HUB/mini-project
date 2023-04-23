# students/apps.py
from django.apps import AppConfig
# from rest_framework import apps

class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'

    # def ready(self):
    #     apps.populate_settings()
    #     apps.populate_apps()
