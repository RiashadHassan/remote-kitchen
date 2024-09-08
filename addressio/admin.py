from django.contrib import admin

from .models import Division, District, Upazila, PostOffice, Address, AddressConnector


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    model = Division
    list_display = ["uid", "name", "bengali_name", "longitude"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["uid", "name", "bengali_name"]
    readonly_fields = ["uid", "created_at", "updated_at"]


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    model = District
    list_display = ["uid", "name", "bengali_name", "longitude", "division"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["uid", "name", "bengali_name", "division"]
    readonly_fields = ["uid", "created_at", "updated_at"]


@admin.register(Upazila)
class UpazilaAdmin(admin.ModelAdmin):
    model = Upazila
    list_display = ["uid", "name", "bengali_name", "district", "division"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["uid", "name", "bengali_name", "district", "division"]
    readonly_fields = ["uid", "created_at", "updated_at"]


@admin.register(PostOffice)
class PostOfficeAdmin(admin.ModelAdmin):
    model = PostOffice
    list_display = [
        "uid",
        "name",
        "code",
        "district",
        "division",
        "upazila",
    ]
    list_filter = ["created_at", "updated_at"]
    search_fields = [
        "uid",
        "name",
        "code",
        "district",
        "division",
        "upazila",
    ]
    readonly_fields = ["uid", "created_at", "updated_at"]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = [
        "uid",
        "label",
        "house_street",
        "upazila",
        "division",
        "district",
        "post_office",
        "country",
    ]
    list_filter = ["created_at", "updated_at"]
    search_fields = [
        "uid",
        "label",
        "house_street",
        "upazila",
        "division",
        "district",
        "post_office",
        "country",
    ]
    readonly_fields = ["uid", "created_at", "updated_at"]


@admin.register(AddressConnector)
class AddressConnectorAdmin(admin.ModelAdmin):
    model = AddressConnector
    list_display = ["uid", "address", "user", "organization"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["uid", "address", "user","organization"]
    readonly_fields = ["uid", "created_at", "updated_at"]
