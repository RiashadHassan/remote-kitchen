from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
)

from core.models import Organization, OrganizationMember
from core.choices import OrganizationStatusChoices, OrganizationMemberStatusChoices
from ..serializers.restaurant import (
    RestaurantListCreateSerializer,
    RestaurantDetailsSerializer,
)

from common.permissions import IsOrganizationOwner, IsOrganizationAdmin


class RestaurantListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RestaurantListCreateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = [
        "name",
        "contact_number",
        "registration_no",
    ]

    def get_queryset(self):

        return Organization.objects.filter(
            status=OrganizationStatusChoices.ACTIVE,
        )


class RestaurantDetailsPublicView(RetrieveAPIView):
    serializer_class = RestaurantDetailsSerializer
    permission_classes = [IsOrganizationOwner, IsOrganizationAdmin]

    def get_queryset(self):
        queryset = Organization.objects.filter(
            status=OrganizationStatusChoices.ACTIVE,
        )

        return queryset

    def get_object(self):
        restaurant_uid = self.kwargs.get("restaurant_uid", None)

        queryset = self.get_queryset()
        restaurant = queryset.get(uid=restaurant_uid)

        return restaurant


class RestaurantDetailsPrivateView(RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantDetailsSerializer
    permission_classes = [IsOrganizationOwner, IsOrganizationAdmin]

    def get_queryset(self):
        queryset = Organization.objects.filter(
            status=OrganizationStatusChoices.ACTIVE,
        )

        return queryset

    def get_object(self):
        restaurant_uid = self.kwargs.get("restaurant_uid", None)

        queryset = self.get_queryset()
        restaurant = queryset.get(uid=restaurant_uid)

        return restaurant

    def perform_destroy(self, instance):
        # making all restaurant members inactive
        OrganizationMember.objects.filter(organization=instance).update(
            status=OrganizationMemberStatusChoices.INACTIVE
        )
        # soft deleting the restaurant
        instance.status = OrganizationStatusChoices.INACTIVE
        instance.save()
