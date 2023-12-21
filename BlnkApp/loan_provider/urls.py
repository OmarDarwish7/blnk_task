from django.urls import path
from . import views


#URLConf
urlpatterns = [
    path('get_all_loan_providers/',views.get_all_loan_providers,name='get_all_loan_providers'),
    path('get_current_budget/',views.get_current_budget,name='get_current_budget')
]