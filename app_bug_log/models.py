from django.db import models


class Topic(models.Model):
    """Bug reported by user"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returning model representation in a form of text string"""
        return self.text
