from django.contrib.auth import get_user_model
from django.db import models

from common.base_model import BaseModelWithUIDSlug
from core.models import Organization

from .choices import MediaKindChoices


User = get_user_model()


# Create your models here.
class MediaRoom(BaseModelWithUIDSlug):
    # image
    image = models.ImageField(
        width_field="width",
        height_field="height",
        null=True,
        blank=True,
    )
    title = models.CharField(blank=True, max_length=500)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)

    # General Information
    file = models.FileField(null=True, blank=True)
    type = models.CharField(
        max_length=50, choices=MediaKindChoices.choices, null=True, blank=True
    )

    def __str__(self):
        return f"{self.id} - UID: {self.uid}, Type: {self.type}"


class MediaRoomConnector(BaseModelWithUIDSlug):
    # Relationship Important
    media_room = models.ForeignKey("mediaroom.MediaRoom", on_delete=models.CASCADE)

    # General Information
    type = models.CharField(max_length=50, choices=MediaKindChoices.choices)

    # Relationship ForeignKey
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.id} - UID: {self.uid}, Type: {self.type}"
