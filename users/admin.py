from django.contrib import admin # type: ignore
from django.contrib.auth.admin import UserAdmin # type: ignore

from django.contrib.auth import get_user_model # type: ignore
from django.utils.translation import gettext_lazy as _ # type: ignore

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    list_display = ("email", 'first_name','last_name',"is_staff", "is_active",'is_superuser')
    list_filter = ("email", "is_staff", "is_active",)
    
    search_fields = ("email","name")
    ordering = ("email",)
    
    fieldsets = (
        (None, {
            "fields": ("email", "password")
            }
        ),
        ("Permissions", 
         {
             "fields": ("is_staff", "is_active", "groups", "user_permissions")
          }
        ),
        (_("Important dates"), 
         {
             "fields": ("last_login", "date_joined")
            }
        ),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )



#admin.site.register(CustomUser, CustomUserAdmin)

# from django.contrib.auth import admin as auth_admin
# from django.contrib.auth import get_user_model


# from google_auth.users.forms import UserChangeForm, UserCreationForm

# User = get_user_model()


# @admin.register(User)
# class UserAdmin(auth_admin.UserAdmin):

#     form = UserChangeForm
#     add_form = UserCreationForm
#     fieldsets = (
#         (None, {"fields": ("username", "password")}),
#         (_("Personal info"), {"fields": ("name", "email")}),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 ),
#             },
#         ),
#         (_("Important dates"), {"fields": ("last_login", "date_joined")}),
#     )
#     list_display = ["username", "name", "is_superuser"]
#     search_fields = ["name"]