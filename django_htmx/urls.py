from django.urls import path # type: ignore

from . import views
app_name = 'dj-htmx'
urlpatterns = [
    path('', views.index ,name='index'),
    path('sub-sectors/', views.get_subsectors, name='get-sub-sectors'),
]