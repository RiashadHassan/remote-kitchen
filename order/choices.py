from django.db import models


class OrderStatus(models.TextChoices):
    ACCEPTED = "ACCEPTED", "Accepted"
    PENDING = "PENDING", "Pending"
    IN_PROGRESS = "IN PROGRESS", "In Progress"
    READY = "READY", "Ready"
    PICKED_UP = "PICKED UP", "Picked Up"
    ON_WAY_TO_DELIVERY = "ON WAY TO DELIVERY", "On Way To Delivery"
    DELIVERED = "DELIVERED", "Delivered"
