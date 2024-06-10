from django import forms
from .models import Bug


class TopicForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ["text"]
        labels = {"text": ""}
