from django.urls import path

from ..views.public import RestaurantMenuListView

urlpatterns = [
    path("", RestaurantMenuListView.as_view(), name="restaurant-menu-list"),
]
