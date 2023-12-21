from django.urls import path
from . import views


#URLConf
urlpatterns = [
    path('add_loan/',views.add_loan,name='add_loan'),
    path('accept_loan/',views.accept_loan,name='accept_loan'),
    path('pay_installment/',views.pay_installment,name='pay_installment'),
    path('get_customer_loans/',views.get_customer_loans,name='get_customer_loans'),
    path('get_all_loans/',views.get_all_loans,name='get_all_loans')
]