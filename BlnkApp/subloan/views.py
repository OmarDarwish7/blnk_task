from django.shortcuts import render
from .models import SubloanModel
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.forms import model_to_dict
# Create your views here.
@csrf_exempt
def get_provider_loans(request):
    try:
        # Assuming the request body contains a JSON object with an 'id' field
        json_data = request.body.decode('utf-8')
        provider_id = json.loads(json_data).get('id')

        # Retrieve all subloans with the specified provider_id
        subloans = SubloanModel.objects.filter(provider_id=provider_id)

        # Convert subloan objects to a list of dictionaries
        subloans_list = [
            {
                'monthly_amount': subloan.monthly_amount,
                'total_amount': subloan.total_amount,
                'current_paid': subloan.current_paid,
                'amount_to_pay': subloan.amount_to_pay,
            }
            for subloan in subloans
        ]

        # Return the JSON response
        return JsonResponse({'subloans': subloans_list}, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
