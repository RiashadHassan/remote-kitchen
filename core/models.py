from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from autoslug import AutoSlugField

from phonenumber_field.modelfields import PhoneNumberField

from common.base_model import BaseModelWithUID, BaseModelWithUIDSlug
from .choices import (
    GenderChoices,
    OrganizationMemberRoleChoices,
    OrganizationStatusChoices,
    OrganizationMemberStatusChoices,
)
from .managers import CustomUserManager
from .utils import get_slug_full_name


class User(AbstractBaseUser, PermissionsMixin, BaseModelWithUIDSlug):
    # General Information
    phone = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(unique=True, db_index=True)
    name = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=20, choices=GenderChoices.choices, default=GenderChoices.UNKNOWN
    )
    location = models.CharField(max_length=200, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Relationship ForeignKey
    media_files = models.ManyToManyField(
        "mediaroom.MediaRoom", through="mediaroom.MediaRoomConnector", blank=True
    )

    # additional settings for User
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name", "phone")

    # Managers
    objects = CustomUserManager()

    def __str__(self):
        name = " ".join([self.first_name, self.last_name])
        data = (
            f"Name: {name}, Email: {self.email}"
            if len(self.email) > 0
            else f"Name: {name} Phone: {self.phone}"
        )

        return f"{self.id} - UID: {self.uid}, {data}"

    def get_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        name = f"{self.first_name} {self.last_name}"
        return name.strip()

    def media_files(self):
        return self.media_files.filter()

    def save(self, *args, **kwargs):
        self.name = f"{self.first_name} {self.last_name}"
        return super().save(*args, **kwargs)


class Organization(BaseModelWithUIDSlug):
    # Basic Information
    name = models.CharField(max_length=255)
    tax_number = models.CharField(max_length=255, blank=True)
    registration_no = models.CharField(max_length=50, blank=True)
    contact_number = PhoneNumberField(blank=True)

    website_url = models.URLField(blank=True)
    blog_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    whatsapp_number = PhoneNumberField(blank=True)

    summary = models.CharField(
        max_length=1000, blank=True, help_text="Short summary about restaurant."
    )
    description = models.CharField(
        max_length=1000, blank=True, help_text="Longer description about restaurant."
    )

    store_front_photo = models.ImageField(
        width_field="width",
        height_field="height",
        null=True,
        blank=True,
        upload_to="images/store_fronts/",
    )
    cover_photo = models.ImageField(
        width_field="width",
        height_field="height",
        null=True,
        blank=True,
        upload_to="images/covers/",
    )
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=OrganizationStatusChoices.choices,
        db_index=True,
        default=OrganizationStatusChoices.ACTIVE,
    )
    short_pitch = models.CharField(max_length=500, blank=True)
    services = models.CharField(
        max_length=800, blank=True, help_text="Services that the company provides"
    )

    location = models.CharField(max_length=200, blank=True, null=True)

    # Relationship ManyToManyField
    addresses = models.ManyToManyField(
        "addressio.Address", through="addressio.AddressConnector", blank=True
    )

    media_files = models.ManyToManyField(
        "mediaroom.MediaRoom", through="mediaroom.MediaRoomConnector", blank=True
    )

    def __str__(self):
        return f"{self.id} - UID: {self.uid}, Slug: {self.slug}"

    def add_owner(self, user: User):
        return OrganizationMember.objects.create(
            organization=self,
            member=user,
            role=OrganizationMemberRoleChoices.OWNER,
            status=OrganizationMemberStatusChoices.ACTIVE,
        )

    def add_admin(self, user: User):
        return OrganizationMember.objects.create(
            organization=self,
            member=user,
            role=OrganizationMemberRoleChoices.ADMIN,
        )

    def is_status_active(self):
        return self.status == OrganizationStatusChoices.ACTIVE

    def set_status_pending(self):
        self.status = OrganizationStatusChoices.PENDING
        self.save()

    def set_status_active(self):
        self.status = OrganizationStatusChoices.ACTIVE
        self.save()


class OrganizationMember(BaseModelWithUID):
    # Relationship Important
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)

    # General Inforamtion
    role = models.CharField(
        max_length=20, choices=OrganizationMemberRoleChoices.choices
    )
    status = models.CharField(
        max_length=20,
        choices=OrganizationMemberStatusChoices.choices,
        default=OrganizationMemberStatusChoices.ACTIVE,
    )

    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ("organization", "member")

    def __str__(self):
        return f"{self.id} - UID: {self.uid}, Role: {self.role}"

    def save_role_admin(self):
        self.role = OrganizationMemberRoleChoices.ADMIN
        self.save()

    def save_role_owner(self):
        self.role = OrganizationMemberRoleChoices.OWNER
        self.save()
