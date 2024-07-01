
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index')
]
