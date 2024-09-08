from django.urls import path, include

urlpatterns = [
    path("public/", include("restaurant.rest.urls.public")),
    path("private/<uuid:restaurant_uid>/", include("restaurant.rest.urls.private")),
]
