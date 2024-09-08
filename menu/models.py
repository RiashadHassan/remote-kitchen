from django.db import models

from common.base_model import BaseModelWithUIDSlug
from common.choices import Status

from core.models import Organization


class Menu(BaseModelWithUIDSlug):
    name = models.CharField(max_length=255)
    status = models.CharField(choices=Status, default=Status.DRAFT)
    restaurant = models.ForeignKey(Organization, on_delete=models.CASCADE)
    tag_line = models.CharField(max_length=1000, blank=True)

    def __str__(self) -> str:
        return f"{self.name} - from: {self.restaurant.name}"


class MenuItem(BaseModelWithUIDSlug):
    name = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=Status, default=Status.DRAFT)

    def __str__(self) -> str:
        return f"{self.name} - from: {self.menu.name}"
