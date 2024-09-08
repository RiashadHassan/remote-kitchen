from django.db import models


class Status(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    INACTIVE = "INACTIVE", "Inactive"
    IN_PROGRESS = "IN PROGRESS", "In Progress"
    DRAFT = "DRAFT", "Draft"
