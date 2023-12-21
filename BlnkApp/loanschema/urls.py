from django.urls import path
from . import views


#URLConf
urlpatterns = [
    path('add_loan_schema/',views.add_loan_schema,name='add_loan_schema'),
    path('get_all_loan_schemas/',views.get_all_loan_schemas,name='get_all_loan_schemas')
]