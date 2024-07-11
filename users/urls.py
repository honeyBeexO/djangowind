from django.urls import path # type: ignore

from users.views import (
    user_detail_view,
    user_redirect_view, 
    user_update_view,
    google_one_tap_login # new
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:email>/", view=user_detail_view, name="detail"),
    path('google_one_tap_login/',view=google_one_tap_login, name='google-one-tap-login' ), # new
]
