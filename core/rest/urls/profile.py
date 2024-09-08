from django.urls import path
from core.rest.views.profile import UserCreateView, UserDetailView

urlpatterns = [
    path("", UserDetailView.as_view(), name="user-details"),
    path("onboarding/", UserCreateView.as_view(), name="user-onboarding"),
]
