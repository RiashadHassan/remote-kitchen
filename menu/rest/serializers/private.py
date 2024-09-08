from django.db import transaction
from rest_framework import serializers

from core.models import Organization
from menu.models import Menu, MenuItem

from common.rest.serializers.slim_serializers import (
    MenuItemPrivateSlimSerializer,
    OrganizationSlimSerializer,
)


class MenuListCreateSerializer(serializers.ModelSerializer):
    items = MenuItemPrivateSlimSerializer(
        source="menuitem_set", many=True, read_only=True
    )
    restaurant = OrganizationSlimSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = [
            "uid",
            "slug",
            "restaurant",
            "name",
            "status",
            "tag_line",
            "items",
        ]
        read_only_fields = [
            "uid",
            "slug",
            "restaurant",
        ]

    @transaction.atomic
    def create(self, validated_data):
        restaurant_uid = self.context["view"].kwargs.get("restaurant_uid", None)

        if restaurant_uid:
            try:
                org = Organization.objects.get(uid=restaurant_uid)
                menu = Menu.objects.create(restaurant=org, **validated_data)

            except Organization.DoesNotExist:
                raise serializers.ValidationError("INVALID UID FOR RESTAURANT")

        return menu


class MenuDetailsSerializer(serializers.ModelSerializer):
    items = MenuItemPrivateSlimSerializer(source="menuitem_set", read_only=True)

    class Meta:
        model = Menu
        fields = [
            "restaurant",
            "name",
            "tag_line",
            "items",
        ]
