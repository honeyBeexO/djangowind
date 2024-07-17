from django.urls import path # type: ignore

from . import views
app_name = 'products'
urlpatterns = [
    path('', views.ProductsListView.as_view(), name='index'),
]