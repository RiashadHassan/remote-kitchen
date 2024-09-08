from django.urls import path
from ..views.private import MenuListCreatePrivateView, MenuDetailsPrivateView

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
]
