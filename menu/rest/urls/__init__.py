from django.urls import path, include
from ..views.public import MenuGlobalListView

urlpatterns = [
    path("menu-list/", MenuGlobalListView.as_view(), name="all-menu"),
    path("public/<uuid:restaurant_slug>/menu/", include("menu.rest.urls.public")),
    path("private/<uuid:restaurant_uid>/menu/", include("menu.rest.urls.private")),
]
