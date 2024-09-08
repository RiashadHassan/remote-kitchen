from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from ..serializers.public import (
    MenuGlobalListSerializer,
    RestaurantMenuListSerializer,
    MenuDetailsPublicSerializer,
    MenuItemGlobalListSerializer,
)
from common.choices import Status
from menu.models import Menu, MenuItem


class MenuGlobalListView(ListAPIView):
    serializer_class = MenuGlobalListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Menu.objects.prefetch_related("menuitem_set").filter(
            status=Status.ACTIVE
        )


class MenuItemGlobalListView(ListAPIView):
    serializer_class = MenuItemGlobalListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Menu.objects.prefetch_related("menuitem_set").filter(
            status=Status.ACTIVE
        )


class RestaurantMenuListView(ListAPIView):
    serializer_class = MenuGlobalListSerializer

    def get_queryset(self):
        restaurant_slug = self.kwargs.get("restaurant_slug", None)

        return (
            Menu.objects.select_related("restaurant")
            .prefetch_related("menuitem_set")
            .filter(
                status=Status.ACTIVE,
                restaurant__slug=restaurant_slug,
            )
        )


class RestaurantMenuDetailsView(RetrieveAPIView):
    serializer_class = RestaurantMenuListSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        restaurant_slug = self.kwargs.get("restaurant_slug", None)
        menu_slug = self.kwargs.get("menu_slug", None)
        return (
            Menu.objects.select_related("restaurant")
            .prefetch_related("menuitem_set")
            .filter(
                status=Status.ACTIVE,
                restaurant__slug=restaurant_slug,
            )
            .get(slug=menu_slug)
        )
