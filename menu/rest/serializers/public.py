from rest_framework import serializers

from common.rest.serializers.slim_serializers import (
    MenuItemPublicSlimSerializer,
    OrganizationSlimSerializer,
)
from menu.models import Menu


class MenuGlobalListSerializer(serializers.ModelSerializer):
    menu_items = MenuItemPublicSlimSerializer(
        source="menuitem_set", read_only=True, many=True
    )

    class Meta:
        model = Menu
        fields = [
            "name",
            "menu_items",
        ]


class RestaurantMenuListSerializer(serializers.ModelSerializer):
    items = MenuItemPublicSlimSerializer(
        source="menuitem_set", many=True, read_only=True
    )
    restaurant = OrganizationSlimSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = [
            "slug",
            "restaurant",
            "name",
            "status",
            "tag_line",
            "items",
        ]
        read_only_fields = [
            "slug",
            "restaurant",
        ]


class MenuDetailsPublicSerializer(serializers.ModelSerializer):
    restaurant = OrganizationSlimSerializer(read_only=True)
    items = MenuItemPublicSlimSerializer(
        source="menuitem_set", read_only=True, many=True
    )

    class Meta:
        model = Menu
        fields = [
            "restaurant",
            "name",
            "tag_line",
            "items",
        ]


class MenuItemGlobalListSerializer(serializers.ModelSerializer):
    pass
