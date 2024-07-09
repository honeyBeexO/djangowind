
from django.contrib import admin # type: ignore
from django.urls import path,include # type: ignore
from .views import index,signin,login,signup,error
from django.conf import settings # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    
    # User management
    path("users/", include("users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    
    path('index/', index, name='index'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('404/', error, name='error'),
    path('buy/', include('payments.urls')), # new
    path('products/', include('products.urls')), # new
]

if settings.DEBUG:
    from django.views import defaults as default_views # type: ignore
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
