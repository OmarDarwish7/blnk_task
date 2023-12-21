from django.urls import path
from . import views


#URLConf
urlpatterns = [
    path('get_provider_loans/',views.get_provider_loans,name='get_provider_loans'),
]