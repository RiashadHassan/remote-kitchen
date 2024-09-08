from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from ..serializers.public import MenuGlobalListSerializer
from common.choices import Status
from menu.models import Menu, MenuItem


class MenuGlobalListView(ListAPIView):
    serializer_class = MenuGlobalListSerializer

    def get_queryset(self):
        return Menu.objects.filter(status=Status.ACTIVE)


class RestaurantMenuListView(ListAPIView):
    serializer_class = MenuGlobalListSerializer

    def get_queryset(self):
        restaurant_slug = self.kwargs.get("restaurant_slug", None)

        return Menu.objects.filter(
            status=Status.ACTIVE,
            restaurant__slug=restaurant_slug,
        ).prefetch_related("menuitems_set")
