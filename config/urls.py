
from django.contrib import admin # type: ignore
from django.urls import path,include # type: ignore
from .views import index,signin,login,signup,error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('404/', error, name='error'),
    path('buy/', include('payments.urls')), # new
    path('products/', include('products.urls')), # new
]
