from django.shortcuts import render
from .models import Bug


def index(request):
    """App home page"""
    return render(request, "app_bug_log/index.html")


def bugs(request):
    """Page with a list of all existing bugs"""
    bugs = Bug.objects.order_by("date_added")
    context = {"bugs": bugs}
    return render(request, "app_bug_log/bugs.html", context)
