from rest_framework.serializers import ModelSerializer

from core.models import User, Organization
from menu.models import MenuItem


class OrganizationSlimSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            "name",
            "slug",
            "uid",
        ]
        read_only_fields = fields


class UserSlimSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "slug",
            "uid",
        ]
        read_only_fields = fields


class MenuItemPublicSlimSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            "name",
            "slug",
            "price",
        ]
        read_only_fields = fields


class MenuItemPrivateSlimSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            "name",
            "uid",
            "slug",
            "price",
        ]
        read_only_fields = fields
