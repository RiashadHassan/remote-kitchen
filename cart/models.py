from django.db import models
from django.contrib.auth import get_user_model

from common.base_model import BaseModelWithUID
from menu.models import MenuItem

User = get_user_model()


class Cart(BaseModelWithUID):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")

    def __str__(self):
        return f"{self.user.username}'s cart"

    def calculate_total_cart_price(self):
        total_price = 0
        for cart_item in self.cart_items.filter():
            total_price += cart_item.calculate_price()
        return total_price


class CartItem(BaseModelWithUID):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    selected = models.BooleanField(default=True)

    class Meta:
        unique_together = ("cart", "menu_item")

    def __str__(self):
        return f"{self.menu_item.name} from {self.menu_item.menu.restaurant.name}"

    @property
    def calculate_price(self):
        return self.menu_item.price * self.quantity
