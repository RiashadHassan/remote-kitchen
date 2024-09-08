from django.urls import path
from ..views.private import (
    MenuListCreatePrivateView,
    MenuDetailsPrivateView,
    MenuItemListCreatePrivateView,
    MenuItemDetailsPrivateView,
)

urlpatterns = [
    path(
        "",
        MenuListCreatePrivateView.as_view(),
        name="list-create-menu",
    ),
    path(
        "<uuid:menu_uid>/",
        MenuDetailsPrivateView.as_view(),
        name="menu-details",
    ),
    path(
        "menu_items/",
        MenuItemListCreatePrivateView.as_view(),
        name="list-create-menu-item",
    ),
    path(
        "<uuid:menu_uid>/menu_items/<uuid:menu_item_uid>/",
        MenuItemDetailsPrivateView.as_view(),
        name="menu-item-details",
    ),
]
