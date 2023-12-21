from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import LoanSchemaModel
import json
from django.http import JsonResponse
from django.forms import model_to_dict
# Create your views here.

@csrf_exempt
def add_loan_schema(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            loanschema = LoanSchemaModel(
                    min_amount = json_data.get('min_amount'),
                    max_amount = json_data.get('max_amount'),
                    interest_rate = json_data.get('interest_rate'),
                    term = json_data.get('term'),
                    bank_percentage = json_data.get('bank_percentage')
                )
            loanschema.save()

            return JsonResponse({'data':model_to_dict(loanschema)},status=200)


        except Exception as e:
            return JsonResponse({'error':str(e)})
   
@csrf_exempt     
def get_all_loan_schemas(request):
    try:
        # Retrieve all loan schema objects
        loan_schemas = LoanSchemaModel.objects.all()

        # Convert loan schema objects to a list of dictionaries
        loan_schemas_list = [
            {
                'min_amount': schema.min_amount,
                'max_amount': schema.max_amount,
                'interest_rate': schema.interest_rate,
                'term': schema.term,
                'bank_percentage': schema.bank_percentage,
            }
            for schema in loan_schemas
        ]

        # Return the JSON response
        return JsonResponse({'loan_schemas': loan_schemas_list}, safe=False)

    except Exception as e:
        # Handle exceptions appropriately
        return JsonResponse({'error': str(e)}, status=500)