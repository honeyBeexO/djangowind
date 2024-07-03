from django.urls import path # type: ignore

from . import views
appname = 'payments'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('config/', views.stripe_config,name='config'),
    path('create-checkout-session/', views.create_checkout_session,name='checkout'),
    path('success/', views.SuccessView.as_view(),name='sucess'), # new
    path('cancelled/', views.CancelledView.as_view(),name='cancel'), # new
    path('webhook/', views.stripe_webhook,name='webhook'), # new
]