from django.db import models


class MediaKindChoices(models.TextChoices):
    IMAGE = "IMAGE", "Image"
    VIDEO = "VIDEO", "Video"
    ATTACHED_FILE = "ATTACHED_FILE", "Attached File"
