from django import forms
from .models import Bug, Comment


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ["title", "description"]
        labels = {"title": "Domain", "description": "Description"}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        labels = {"text": "Comment: "}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
