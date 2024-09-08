from django.urls import path

from ..views.restaurant import RestaurantListCreateView, RestaurantDetailsPublicView

urlpatterns = [
    path("", RestaurantListCreateView.as_view(), name="list-create-restaurants"),
    path(
        "<uuid:restaurant_slug>/",
        RestaurantDetailsPublicView.as_view(),
        name="public-restaurant-details",
    ),
]
