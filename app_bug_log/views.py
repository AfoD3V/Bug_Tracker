from django.shortcuts import render, redirect
from .models import Bug, Comment
from .forms import BugForm, CommentForm


def index(request):
    """App home page"""
    return render(request, "app_bug_log/index.html")


def bugs(request):
    """Page with a list of all existing bugs"""
    bugs = Bug.objects.order_by("date_added")
    context = {"bugs": bugs}
    return render(request, "app_bug_log/bugs.html", context)


def bug(request, bug_id):
    """Single bug page"""
    bug = Bug.objects.get(id=bug_id)
    # Getting all the comments for particular bug
    comments = bug.comment_set.order_by("-date_added")
    context = {"bug": bug, "comments": comments}
    return render(request, "app_bug_log/comment.html", context)


def new_bug(request):
    """Adding new bug"""
    if request.method != "POST":
        # Data is not provided, create new form
        form = BugForm()
    else:
        # Data has been provided - procees following data
        form = BugForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("app_bug_log:bugs")

    # displaying empty form
    context = {"form": form}
    return render(request, "app_bug_log/new_bug.html", context)


def new_comment(request, bug_id):
    """Adding new comment for specific bug"""
    bug = Bug.objects.get(id=bug_id)

    if request.method != "POST":
        # Data is not provided, create new form
        form = CommentForm()
    else:
        # Data has been provided - procees following data
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.bug = bug
            new_comment.save()
            return redirect("app_bug_log:comment", bug_id=bug_id)

    # display empty form
    context = {"bug": bug, "form": form}
    return render(request, "app_bug_log/new_comment.html", context)


def edit_comment(request, comment_id):
    """Editing existing comment"""
    comment = Comment.objects.get(id=comment_id)
    bug = comment.bug

    if request.method != "POST":
        # initial request for filling form
        form = CommentForm(instance=comment)
    else:
        # POST method was requested, data has to be processed
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("app_bug_log:bug", bug_id=bug.id)

    # display empty form
    context = {"comment": comment, "bug": bug, "form": form}
    return render(request, "app_bug_log/edit_comment.html", context)
