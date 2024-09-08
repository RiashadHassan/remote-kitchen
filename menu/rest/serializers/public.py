from rest_framework.serializers import ModelSerializer

from common.rest.serializers.slim_serializers import MenuItemPublicSlimSerializer
from menu.models import Menu


class MenuGlobalListSerializer(ModelSerializer):
    menu_items = MenuItemPublicSlimSerializer(source="menuitem_set", read_only=True)

    class Meta:
        model = Menu
        fields = [
            "name",
            "menu_items",
        ]
