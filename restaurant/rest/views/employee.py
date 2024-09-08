from rest_framework.generics import (
    get_object_or_404,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from core.models import User, Organization, OrganizationMember
from core.choices import OrganizationStatusChoices, OrganizationMemberStatusChoices
from ..serializers.employee import (
    EmployeeListCreateSerializer,
    EmployeeDetailsSerializer,
)
from common.permissions import IsOrganizationOwner, IsOrganizationAdmin


class EmployeeListCreatePrivateView(ListCreateAPIView):
    permission_classes = [IsOrganizationOwner, IsOrganizationAdmin]
    serializer_class = EmployeeListCreateSerializer

    def get_queryset(self):
        return OrganizationMember.objects.filter(
            status=OrganizationMemberStatusChoices.ACTIVE,
        )


class EmployeeDetailsPrivateView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeDetailsSerializer
    permission_classes = [IsOrganizationOwner, IsOrganizationAdmin]

    def get_object(self):
        """
        we are using the restaurant_uid to ensure that we dont get employee details even
        when the url has an invalid uid for restaurant
        """

        restaurant_uid = self.kwargs.get("restaurant_uid", None)
        employee_uid = self.kwargs.get("employee_uid", None)
        member = get_object_or_404(
            OrganizationMember, organization__uid=restaurant_uid, uid=employee_uid
        )

        return member

    def perform_destroy(self, instance):
        # making all restaurant members inactive
        OrganizationMember.objects.filter(organization=instance).update(
            status=OrganizationMemberStatusChoices.INACTIVE
        )
        # soft deleting the restaurant
        instance.status = OrganizationStatusChoices.INACTIVE
        instance.save()
