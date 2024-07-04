from django.urls import path # type: ignore

from . import views
appname = 'products'
urlpatterns = [
    path('', views.ProductsListView.as_view(), name='index'),
]