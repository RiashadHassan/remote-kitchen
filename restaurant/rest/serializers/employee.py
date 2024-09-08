from django.db import transaction

from rest_framework import serializers
from core.models import User, Organization, OrganizationMember
from common.rest.serializers.slim_serializers import (
    UserSlimSerializer,
    OrganizationSlimSerializer,
)


class EmployeeListCreateSerializer(serializers.ModelSerializer):
    member = UserSlimSerializer(read_only=True)
    organization = OrganizationSlimSerializer(read_only=True)
    user_uid = serializers.UUIDField(write_only=True, required=True)

    class Meta:
        model = OrganizationMember
        fields = [
            "uid",
            "organization",
            "member",
            "role",
            "status",
            "user_uid",
        ]
        read_only_fields = [
            "uid",
            "organization",
            "member",
        ]

    @transaction.atomic
    def create(self, validated_data):
        organization_uid = self.context["view"].kwargs.get("restaurant_uid", None)
        user_uid = validated_data.pop("user_uid", None)
        if user_uid and organization_uid:
            try:
                org = Organization.objects.get(uid=organization_uid)
                user = User.objects.get(uid=user_uid)

                # check if user is already a member of this organization
                org_member = OrganizationMember.objects.filter(
                    organization=org, member=user
                ).first()

                if org_member:
                    raise serializers.ValidationError("Member already exists!")

                member = OrganizationMember.objects.create(
                    member=user, organization=org, **validated_data
                )
            except User.DoesNotExist:
                raise serializers.ValidationError("INVALID UID FOR USER")

        return member


class EmployeeDetailsSerializer(serializers.ModelSerializer):
    member = UserSlimSerializer(read_only=True)
    organization = OrganizationSlimSerializer(read_only=True)

    class Meta:
        model = OrganizationMember
        fields = [
            "uid",
            "organization",
            "member",
            "role",
            "status",
        ]
        read_only_fields = [
            "uid",
        ]
