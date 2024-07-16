from django.shortcuts import render # type: ignore

from django.contrib.auth import get_user_model # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin # type: ignore
from django.contrib.messages.views import SuccessMessageMixin # type: ignore
from django.urls import reverse # type: ignore
from django.utils.translation import gettext_lazy as _ # type: ignore
from django.views.generic import DetailView, RedirectView, UpdateView # type: ignore

from django.views.decorators.csrf import csrf_exempt # type: ignore
from django.http import HttpResponseRedirect # type: ignore
LOCAL_DOMAIN = 'localhost:8000'

CustomUser = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    
    model = CustomUser
    template_name = 'users/customuser_detail.html'
    context_object_name = 'user'
    slug_field = "uuid"
    slug_url_kwarg = "uuid"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = CustomUser
    fields = ("email",)
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.request.user.get_absolute_url()  # type: ignore [union-attr]
    # def get_success_url(self):
    #     return reverse("users:detail", kwargs={"uuid": self.request.user.uuid})

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"uuid": self.request.user.uuid})


user_redirect_view = UserRedirectView.as_view()

@csrf_exempt
def google_one_tap_login(request):
    login_url = LOCAL_DOMAIN + '/accounts/google/login/'
    return HttpResponseRedirect(login_url)