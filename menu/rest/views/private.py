from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..serializers.private import MenuListCreateSerializer, MenuDetailsSerializer
from common.choices import Status
from common.permissions import IsOrganizationOwner, IsOrganizationAdmin
from menu.models import Menu, MenuItem


class MenuListCreatePrivateView(ListCreateAPIView):
    serializer_class = MenuListCreateSerializer
    permission_classes = [IsOrganizationOwner, IsOrganizationAdmin]

    def get_queryset(self):
        restaurant_uid = self.kwargs.get("restaurant_uid", None)
        return Menu.objects.filter(
            status=Status.ACTIVE,
            restaurant__uid=restaurant_uid,
        ).prefetch_related("menuitem_set")


class MenuDetailsPrivateView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuDetailsSerializer
    permission_classes = [IsOrganizationOwner, IsOrganizationAdmin]

    def get_object(self):
        restaurant_uid = self.kwargs.get("restaurant_uid", None)
        menu_uid = self.kwargs.get("menu_uid", None)
        return (
            Menu.objects.prefetch_related("menuitem_set")
            .filter(
                restaurant__uid=restaurant_uid,
            )
            .get(
                uid=menu_uid,
            )
        )

    def perform_destroy(self, instance):
        # soft deleting the menu
        instance.status = Status.INACTIVE
        instance.save()
