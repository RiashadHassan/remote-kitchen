from django.urls import path

from ..views.public import RestaurantMenuListView, RestaurantMenuDetailsView

urlpatterns = [
    path("", RestaurantMenuListView.as_view(), name="restaurant-menu-list"),
    path(
        "<slug:menu_slug>/",
        RestaurantMenuDetailsView.as_view(),
        name="restaurant-menu-details",
    ),
]
