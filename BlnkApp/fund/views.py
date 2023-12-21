from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import FundModel
from loan_provider.models import LoanProviderModel
import json
from django.forms import model_to_dict
from django.http import JsonResponse , HttpResponse
from django.utils import timezone
import loan_provider.loan_provider_service as LoanProviderService
# Create your views here.

@csrf_exempt
def add_fund(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body.decode('utf-8'))

            loan_provider = LoanProviderModel.objects.get(pk= json_data.get('provider'))
            

            fund = FundModel(
                provider = loan_provider,
                amount = json_data.get('amount'),
                date = timezone.now().date()
            )

            fund.save()

            LoanProviderService.increase_total_funds(json_data.get('provider'),fund.amount)

            response_data = model_to_dict(fund)

            return JsonResponse({'data' : response_data},status=200)
        
        except Exception as e:
            return JsonResponse({'error':str(e)})

@csrf_exempt
def get_provider_funds(request):
    try:
        # Assuming the request body contains a JSON object with a 'provider_id' field
        json_data = request.body.decode('utf-8')
        provider_id = json.loads(json_data).get('provider_id')

        # Retrieve all funds with the specified provider_id
        provider_funds = FundModel.objects.filter(provider_id=provider_id)

        # Convert fund objects to a list of dictionaries
        provider_funds_list = [
            {
                'amount': fund.amount,
                'date': fund.date.strftime('%Y-%m-%d'),  # Format date as string
            }
            for fund in provider_funds
        ]

        # Return the JSON response
        return JsonResponse({'provider_funds': provider_funds_list}, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)