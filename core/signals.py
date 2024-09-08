from django.dispatch import receiver
from django.db.models.signals import post_save

from core.models import User
from cart.models import Cart
