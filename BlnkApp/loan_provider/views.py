from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import LoanProviderModel
from django.http import JsonResponse
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.db.models import Sum

# Create your views here.
@csrf_exempt
def get_all_loan_providers(request):
    if request.method == 'GET':
        all_instances = LoanProviderModel.objects.all()

        instances_list = [model_to_dict(instance) for instance in all_instances]

        # Return JSON response
        return JsonResponse({'data': instances_list}, safe=False)
    
@csrf_exempt
def get_current_budget(request):
    return JsonResponse({'budget':get_total_budget()},status = 200)

def get_total_budget():
    try:
        total_budget = LoanProviderModel.objects.aggregate(total=Sum('current_total_funds'))['total']

        if total_budget is not None:
            return total_budget
    except Exception as e:
        return str(e)