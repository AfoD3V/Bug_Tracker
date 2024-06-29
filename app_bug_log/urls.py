"""This module is a config to define URLS for app_bug_logs"""

from django.urls import path
from . import views

app_name = "app_bug_log"
urlpatterns = [
    # home page
    path("", views.index, name="index"),
    # bug list page
    path("bugs/", views.bugs, name="bugs"),
    # single bug page
    path("bugs/<str:bug_id>/", views.bug, name="bug"),
    # new bug page
    path("new_bug/", views.new_bug, name="new_bug"),
    # new comment
    path("new_comment/<str:bug_id>/", views.new_comment, name="new_comment"),
    # edit comment
    path("edit_comment/<int:comment_id>/", views.edit_comment, name="edit_comment"),
]
