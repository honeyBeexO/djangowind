from django.contrib import admin # type: ignore
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin # type: ignore
from .models import CustomUser, Profile, Address
from django.utils.translation import gettext_lazy as _ # type: ignore
from django.utils.html import format_html # type: ignore

from unfold.admin import ModelAdmin # type: ignore


class HomeAddressInline(admin.StackedInline):
    model = Address
    fk_name = 'user_home_address'
    extra = 0
    max_num = 1
    can_delete = False
    verbose_name_plural = 'Home Addresses'

class BusinessAddressInline(admin.StackedInline):
    model = Address
    fk_name = 'user_business_address'
    extra = 0
    max_num = 1
    can_delete = False
    verbose_name_plural = 'Business Addresses'

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ('user', 'get_email', 'get_phone_number', 'get_profile_image')
    search_fields = ('user__email', 'user__phone_number')  # Search through User's phone_number

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = _("Email")

    def get_phone_number(self, obj):
        return obj.user.phone_number  # Retrieve phone number from User
    get_phone_number.short_description = _("Phone Number")

    def get_profile_image(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="50" height="50" />', obj.profile_image.url)
        return "No Image"
    get_profile_image.short_description = _("Profile Image")
    
@admin.register(Address)
class AddressAdmin(ModelAdmin):
    list_display = ('name', 'street_address', 'postal_code', 'city', 'country')
    list_filter = ('country', 'city')
    search_fields = ('name', 'street_address', 'postal_code', 'city')
    ordering = ('name', 'country', 'city')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name',)
        }),
        ('Address Details', {
            'fields': ('street_address', 'postal_code', 'city', 'country')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ('created_at', 'updated_at')
    

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin, ModelAdmin):
    inlines = (ProfileInline,)
    list_display = ("email", "get_full_name", "phone_number", "is_staff", "is_active", "is_superuser",'home_address','business_address',)
    search_fields = ("email", "first_name", "last_name", "phone_number")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "phone_number")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Important Addresses", {"fields": ("home_address", "business_address")}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "first_name", "last_name", "phone_number", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    get_full_name.short_description = "Full Name"