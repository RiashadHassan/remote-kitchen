from django.db import transaction

from rest_framework.serializers import Serializer, ModelSerializer

from core.models import Organization, OrganizationMember


class RestaurantListCreateSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            "name",
            "uid",
            "slug",
            "tax_number",
            "registration_no",
            "contact_number",
            "website_url",
            "blog_url",
            "instagram_url",
            "facebook_url",
            "twitter_url",
            "whatsapp_number",
            "summary",
            "description",
            "store_front_photo",
            "width",
            "height",
            "status",
            "short_pitch",
            "services",
            "location",
            "addresses",
            "media_files",
        ]
        read_only_fields = ["uid", "slug"]

    @transaction.atomic
    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.add_owner(self.context["request"].user)
        return instance


class RestaurantDetailsSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            "name",
            "uid",
            "slug",
            "tax_number",
            "registration_no",
            "contact_number",
            "website_url",
            "blog_url",
            "instagram_url",
            "facebook_url",
            "twitter_url",
            "whatsapp_number",
            "summary",
            "description",
            "store_front_photo",
            "width",
            "height",
            "status",
            "short_pitch",
            "services",
            "location",
            "addresses",
            "media_files",
        ]
        read_only_fields = ["uid", "slug"]
