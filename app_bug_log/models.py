from django.db import models
from enum import Enum
import uuid


class Status(Enum):
    """Status choice field classs"""

    NEW = "New"
    ANALYZING = "Analyzing"
    IN_PROGRESS = "In Progress"
    FIXED = "Fixed"
    RETEST = "Re-test"
    DONE = "Done"


class Priority(Enum):
    """Priority choice field classs"""

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Severity(Enum):
    """Severity choice field classs"""

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


def enums_to_choice(enum_class):
    return [(tag.name, tag.value) for tag in enum_class]


class Bug(models.Model):
    """Bug reported by user."""

    # Constants
    STATUS_CHOICES = enums_to_choice(Status)
    PRIORITY_CHOICES = enums_to_choice(Priority)
    SEVERITY_CHOICES = enums_to_choice(Severity)

    # Fields
    id = models.CharField(max_length=20, primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    attachment = models.FileField(upload_to="bug_attachments/", blank=True, null=True)

    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=12,
        default=STATUS_CHOICES[0][1],  # New
    )

    severity = models.CharField(
        choices=SEVERITY_CHOICES,
        max_length=8,
        default=SEVERITY_CHOICES[1][1],  # Medium
    )

    priority = models.CharField(
        choices=PRIORITY_CHOICES,
        max_length=6,
        default=PRIORITY_CHOICES[1][1],  # Medium
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generate_unique_id()
        super().save(*args, **kwargs)

    def generate_unique_id(self):
        while True:
            new_id = str(uuid.uuid4())[:8]
            if not Bug.objects.filter(id=new_id).exists():
                return new_id

    def __str__(self):
        """Returning Bug id/title with description"""
        return f"{self.id}: [{self.title}] - {self.description}"
