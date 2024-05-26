from django.shortcuts import render


def index(request):
    """App home page"""
    return render(request, "app_bug_log/index.html")
