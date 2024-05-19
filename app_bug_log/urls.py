"""This module is a config to define URLS for app_bug_logs"""

from django.urls import path
from . import views

app_name = "app_bug_log"
urlpatterns = [
    # home page
    path("", views.index, name="index"),
]
