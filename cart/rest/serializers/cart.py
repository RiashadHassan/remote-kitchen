from django.shortcuts import get_object_or_404

from rest_framework import serializers


from cart.models import Cart, CartItem
from menu.models import Menu, MenuItem


class ManageCartItemSerializer(serializers.ModelSerializer):
    menu_item = serializers.uidField(source="menu_item.uid", read_only=True)
    cart_item_total_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        source="calculate_price",
    )

    class Meta:
        model = CartItem
        fields = [
            "uid",
            "menu_item",
            "quantity",
            "cart_item_total_price",
            "selected",
        ]


class ListCreateCartItemSerializer(serializers.ModelSerializer):
    menu_item_slug = serializers.SlugField(source="menu_item.slug", read_only=True)
    cart_item_total_price = serializers.SerializerMethodField()
    selected = serializers.BooleanField(default=True)
    menu_item_uid = serializers.uidField(write_only=True)

    class Meta:
        model = CartItem
        fields = [
            "uid",
            "menu_item_uid",
            "menu_item_slug",
            "quantity",
            "cart_item_total_price",
            "selected",
        ]

    def get_cart_item_total_price(self, obj):
        return obj.calculate_price()

    def create(self, validated_data):
        menu_item_uid = validated_data.get("menu_item_uid")
        menu_item = get_object_or_404(MenuItem, uid=menu_item_uid)

        cart = self.context["request"].user.cart

        # if CartItem.objects.get(menu_item=menu_item, cart=cart):
        #     raise serializers.ValidationError("MenuItem already exists in cart")

        quantity = validated_data.get("quantity")

        if menu_item.menu_iteminventory.quantity < quantity:
            raise serializers.ValidationError("Not enough quantity in stock")

        cart_item = CartItem.objects.create(
            cart=cart, menu_item=menu_item, quantity=quantity
        )

        return cart_item

    def validate(self, data):
        if "quantity" in data and data["quantity"] < 1:
            raise serializers.ValidationError("Quantity must be at least 1")
        return data


class CartSerializer(serializers.ModelSerializer):
    cart_items = ManageCartItemSerializer(
        many=True,
        read_only=True,
        fields=("uid", "menu_item", "quantity", "cart_item_total_price"),
    )
    cart_total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["cart_total_price", "cart_items"]
        read_only_fields = ["uid"]

    def get_cart_total_price(self, obj):
        return obj.calculate_total_cart_price()
