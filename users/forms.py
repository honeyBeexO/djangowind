from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm # type: ignore
from django.contrib.auth import get_user_model # type: ignore
from django.utils.translation import gettext_lazy as _ # type: ignore

CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)
        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
            "email": {"unique": _("This email has already been taken.")}
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)



# User = get_user_model()


# class UserChangeForm(admin_forms.UserChangeForm):
#     class Meta(admin_forms.UserChangeForm.Meta):
#         model = User


# class UserCreationForm(admin_forms.UserCreationForm):
#     class Meta(admin_forms.UserCreationForm.Meta):
#         model = User

#         error_messages = {
#             "username": {"unique": _("This username has already been taken.")},
#             "email": {"unique": _("This email has already been taken.")}
#         }