from rest_framework import serializers

from core.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uid",
            "slug",
            "email",
            "first_name",
            "last_name",
            "gender",
            "phone",
            "date_of_birth",
            "location",
            "password",
        ]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 10,
            }
        }
        read_only_fields = ["uid", "slug"]


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uid",
            "slug",
            "email",
            "first_name",
            "last_name",
            "gender",
            "phone",
            "date_of_birth",
            "location",
            "password",
        ]

        read_only_fields = ["uid", "slug"]
