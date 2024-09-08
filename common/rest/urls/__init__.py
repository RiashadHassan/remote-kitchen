from django.urls import path, include

urlpatterns = [
    path("", include("rest_framework.urls")),
    path("auth/", include("common.rest.urls.auth")),
    path("swagger/", include("common.rest.urls.swagger")),
    path("silk/", include("silk.urls", namespace="silk")),
]
