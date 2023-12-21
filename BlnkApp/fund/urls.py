from django.urls import path
from . import views


#URLConf
urlpatterns = [
    path('add_fund/',views.add_fund,name='add_fund'),
    path('get_provider_funds/',views.get_provider_funds,name='get_provider_funds')
]