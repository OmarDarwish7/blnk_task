from django.urls import path
from . import views


#URLConf
urlpatterns = [
    path('add_user/',views.add_user,name='add_user'),
    path('login/',views.login,name='login')
]