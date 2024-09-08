from django.urls import path, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # django admin panel
    path("admin/", admin.site.urls),
    # swagger, JWT, Silk and other important stuff
    path("api/common/", include("common.rest.urls")),
    # user specific endpoints
    path("api/v1/me/", include("core.rest.urls")),
    # employee/specific eendpoints
    path("api/v1/restaurants/", include("restaurant.rest.urls")),
    path("api/v1/", include("menu.rest.urls")),
    # path("api/v1/orders/", include("order.rest.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
