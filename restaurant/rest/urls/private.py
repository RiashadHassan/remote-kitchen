from django.urls import path

from ..views.restaurant import RestaurantDetailsPrivateView
from ..views.employee import EmployeeListCreatePrivateView, EmployeeDetailsPrivateView

urlpatterns = [
    path(
        "",
        RestaurantDetailsPrivateView.as_view(),
        name="restaurant-details",
    ),
    path(
        "employees/",
        EmployeeListCreatePrivateView.as_view(),
        name="list-create-employees",
    ),
    path(
        "employees/<uuid:employee_uid>/",
        EmployeeDetailsPrivateView.as_view(),
        name="employee-details",
    ),
]
