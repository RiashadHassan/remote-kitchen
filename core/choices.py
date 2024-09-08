from django.db import models


class GenderChoices(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"
    OTHER = "OTHER", "Other"
    UNKNOWN = "UNKNOWN", "Unknown"


class OrganizationStatusChoices(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PLACEHOLDER = "PLACEHOLDER", "Placeholder"
    PENDING = "PENDING", "Pending"
    ACTIVE = "ACTIVE", "Active"
    INACTIVE = "INACTIVE", "Inactive"
    REMOVED = "REMOVED", "Removed"


class OrganizationMemberRoleChoices(models.TextChoices):
    OWNER = "OWNER", "Owner"
    ADMIN = "ADMIN", "Admin"
    CHEF = "CHEF", "Chef"
    STAFF = "STAFF", "Staff"
    WAITER = "WAITER", "Waiter"
    SECURITY = "SECURITY", "Security"


class OrganizationMemberStatusChoices(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    INACTIVE = "INACTIVE", "Inactive"
    PENDING = "PENDING", "PENDING"
    SUSPENDED = "SUSPENDED", "Suspended"
    FIRED = "Fired", "Fired"
