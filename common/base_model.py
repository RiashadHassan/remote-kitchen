import uuid

from django.db import models

from django.utils import timezone

from autoslug import AutoSlugField


class BaseModelWithUID(models.Model):
    uid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, db_index=True
    )

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class BaseModelWithUIDSlug(BaseModelWithUID):
    slug = AutoSlugField(
        populate_from="name", unique=True, unique_with="name", editable=False, null=True
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
