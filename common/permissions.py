from django.contrib.auth import get_user_model

from rest_framework.permissions import BasePermission

from core.choices import OrganizationMemberRoleChoices, OrganizationMemberStatusChoices
from core.models import Organization, OrganizationMember

permitted_statuses = [
    OrganizationMemberStatusChoices.PENDING,
    OrganizationMemberStatusChoices.ACTIVE,
]

User = get_user_model()


class IsOrganizationOwner(BasePermission):
    """
    Only Owner can access this owner permission
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        organization_uid = view.kwargs.get("restaurant_uid", None)

        try:
            organization = Organization.objects.get(uid=organization_uid)
            OrganizationMember.objects.get(
                organization=organization,
                member=request.user,
                role=OrganizationMemberRoleChoices.OWNER,
            )
        except (Organization.DoesNotExist, OrganizationMember.DoesNotExist):
            return False

        return True


class IsOrganizationAdmin(BasePermission):
    """
    Only Owner or Admin can access this admin permission
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        organization_uid = view.kwargs.get("restaurant_uid", None)

        try:
            organization = Organization.objects.get(uid=organization_uid)
            OrganizationMember.objects.get(
                organization=organization,
                member=request.user,
                role__in=[
                    OrganizationMemberRoleChoices.ADMIN,
                    OrganizationMemberRoleChoices.OWNER,
                ],
            )
        except (Organization.DoesNotExist, OrganizationMember.DoesNotExist):
            return False

        return True
