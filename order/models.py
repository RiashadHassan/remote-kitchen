from django.db import models
from django.contrib.auth import get_user_model

from common.base_model import BaseModelWithUIDSlug
from menu.models import Menu, MenuItem

from .choices import OrderStatus
from .utils import generate_random_order_no

User = get_user_model()


class Order(BaseModelWithUIDSlug):
    order_no = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=100, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_status = models.CharField(
        max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING
    )

    def calculate_total_order_price(self):
        total_price = 0
        for order_item in self.order_items.filter():
            total_price += order_item.calculate_price()
        return total_price

    def __str__(self):
        return f"Order no {self.uuid}"

    def generate_order_no(self):
        new_order_no = generate_random_order_no()
        try:
            Order.objects.get(order_no=new_order_no)
            return self.generate_order_no()
        except Order.DoesNotExist:
            self.order_no = new_order_no
            self.save()
            return self.order_no


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.menu_item.name} from {self.menu_item.menu.restaurant.name}"

    def calculate_price(self):
        return self.menu_item.price * self.quantity

    def save(self, *args, **kwargs):
        self.price = self.calculate_price()
        super().save(*args, **kwargs)
