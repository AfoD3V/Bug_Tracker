from django.db import models
from enum import Enum


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
    bug_id = models.AutoField(primary_key=True, default="00000")
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

    def __str__(self):
        """Returning Bug id/title with description"""
        return f"{self.bug_id}:{self.title} - {self.description}"
