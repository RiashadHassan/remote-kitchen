from django.db.models.signals import post_save
from django.dispatch import receiver

from order.models import Order


@receiver(post_save, sender=Order)
def send_mail(sender, instance, created, **kwargs):
    if created:
        pass
        # if time had allowed i would have used celery to sent mail via smtp
