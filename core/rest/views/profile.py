from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


from core.models import User, OrganizationMember
from core.choices import OrganizationMemberStatusChoices
from core.rest.serializers.profile import UserCreateSerializer, UserDetailsSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = User.objects.get(pk=self.request.user.pk)
        return user

    def perform_destroy(self, instance):
        # deactivating the user account
        instance.is_active = False
        instance.save()

        OrganizationMember.objects.filter(user=instance).update(
            status=OrganizationMemberStatusChoices.INACTIVE
        )
