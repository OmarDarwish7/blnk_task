from django.forms import model_to_dict
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import LoanModel
import json 
from django.http import HttpResponse
from django.http import JsonResponse
from users.models import UserModel
import loan_provider.loan_provider_service as LoanProviderService
import loanschema.loanschema_service as LoanSchemaService
import subloan.subloan_service as SubLoanService
from django.core.serializers import serialize

# Create your views here.

@csrf_exempt
def get_all_loans(request):
    try:
        # Retrieve all loan objects
        loans = LoanModel.objects.all()

        # Convert loan objects to a list of dictionaries
        loans_list = [
            {
                'requested_amount': loan.requested_amount,
                'interest_rate': loan.interest_rate,
                'amount_after_interest': loan.amount_after_interest,
                'amount_paid': loan.amount_paid,
                'amount_to_pay': loan.amount_to_pay,
                'monthly_amount': loan.monthly_amount,
                'bank_percentage': loan.bank_percentage,
                'term': loan.term,
                'status': loan.status,
                'id':loan.id
            }
            for loan in loans
        ]

        # Return the JSON response
        return JsonResponse({'loans': loans_list}, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
@csrf_exempt
def add_loan(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body.decode('utf-8'))

            customer_instance = UserModel.objects.get(pk=json_data.get('customer'))
            # customer , amount

            schema = LoanSchemaService.get_loan_schema(json_data.get('amount'))

            if schema != '404':
                print(schema)
                loan = LoanModel(
                    customer= customer_instance,
                    requested_amount = json_data.get('amount'),
                    interest_rate = schema['interest_rate'],
                    amount_after_interest = json_data.get('amount') + (json_data.get('amount')* (schema['interest_rate']/100)),
                    amount_paid = 0.0,
                    amount_to_pay = json_data.get('amount') + (json_data.get('amount')* (schema['interest_rate']/100)),
                    monthly_amount = (json_data.get('amount') + (json_data.get('amount')* (schema['interest_rate']/100))) / schema['term'],
                    bank_percentage = schema['bank_percentage'],
                    term = schema['term'],
                    status = 'Pending'
                )

                # loan = LoanModel(
                #     customer= customer_instance,
                #     requested_amount = json_data.get('requested_amount'),
                #     interest_rate = json_data.get('interest_rate'),
                #     amount_after_interest = json_data.get('requested_amount') + (json_data.get('requested_amount')* (json_data.get('interest_rate')/100)),
                #     amount_paid = 0.0,
                #     amount_to_pay = json_data.get('requested_amount') + (json_data.get('requested_amount')* (json_data.get('interest_rate')/100)),
                #     monthly_amount = (json_data.get('requested_amount') + (json_data.get('requested_amount')* (json_data.get('interest_rate')/100))) / json_data.get('term'),
                #     bank_percentage = json_data.get('bank_percentage'),
                #     term = json_data.get('term'),
                #     status = 'Pending'
                #     )
                
                loan.save()

                response_data = model_to_dict(loan)

                return JsonResponse({'data' : response_data},status=200)
            
            return JsonResponse({'message':'No schema applicable to requested amount'},status = 400) 
            
        except Exception as e:
            return JsonResponse({'error':str(e)})
            


@csrf_exempt
def get_customer_loans(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body.decode('utf-8'))

            loans = LoanModel.objects.filter(customer_id = json_data.get('id'))

            loans_list = [
                    {
                        'requested_amount': loan.requested_amount,
                        'interest_rate': loan.interest_rate,
                        'amount_after_interest': loan.amount_after_interest,
                        'amount_paid': loan.amount_paid,
                        'amount_to_pay': loan.amount_to_pay,
                        'monthly_amount': loan.monthly_amount,
                        'bank_percentage': loan.bank_percentage,
                        'term': loan.term,
                        'status': loan.status,
                        'customer': loan.customer.id,  # Assuming customer is a ForeignKey
                        'id':loan.id
                    }
            for loan in loans
            ]

            # Return the JSON response
            return JsonResponse({'data': loans_list}, safe=False)

        except Exception as e:
            return JsonResponse({'error':str(e)})



@csrf_exempt
def accept_loan(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            
            loan = LoanModel.objects.get(pk=json_data.get('id'))


            if loan is not None:
                if loan.status == 'Pending':
                    total_budget = LoanProviderService.get_total_budget()

                    if loan.requested_amount <= total_budget:
                        interest_amount = float(loan.amount_after_interest) - float(loan.requested_amount)
                        amount_after_interest = loan.amount_after_interest
                        bank_amount = float(interest_amount) * (float(loan.bank_percentage) / 100)
                        amount_for_providers = amount_after_interest - bank_amount
                        provider_shares = LoanProviderService.get_shares()

                        for share in provider_shares:
                            provider_loan_amount = float(share.get('share')) * float(amount_for_providers)
                            print(provider_loan_amount)

                            subloan_response = SubLoanService.create_subloan(subloan_object={
                                    'share_of_total' : share.get('share'),
                                    'monthly_amount': float(provider_loan_amount) / float(loan.term),
                                    'total_amount': provider_loan_amount,
                                    'loan': loan,
                                    'customer': loan.customer,
                                    'provider': share.get('id')
                                })
                            if subloan_response != 'success':
                                return JsonResponse({'message':subloan_response})
                            decrease_response = LoanProviderService.decrease_total_funds(share.get('id').id_id,float(share.get('share') * float(loan.requested_amount)))
                            # if decrease_response != 'success':
                            #     print(f'decrease response {decrease_response}')

                            
                        loan.status = 'Accepted'
                        loan.save()

                        json_loan = model_to_dict(loan)

                        return JsonResponse({'data':json_loan},status=200)
                    else:
                        return JsonResponse({'message':'Insufficient Funds'})

                    
                else:
                    return JsonResponse({'message':'Loan status not Pending'})


            
                
        except Exception as e:
            return JsonResponse({'message':{str(e)}})

@csrf_exempt     
def pay_installment(request):
        if request.method == 'POST':
            try:
                json_data = json.loads(request.body.decode('utf-8'))

                customer_id = json_data.get('customer_id')

                # loan id
                loan = LoanModel.objects.get(pk = json_data.get('loan_id'))

                if loan.customer.id == customer_id:
                    
                    if loan.amount_to_pay > 0:
                        loan.amount_paid += loan.monthly_amount
                        loan.amount_to_pay -= loan.monthly_amount

                        if loan.amount_to_pay < 0:
                            loan.status = 'Done'
                            loan.amount_to_pay = 0
                            loan.amount_paid = loan.amount_after_interest

                        loan.save()

                        subloan_response = SubLoanService.pay_installments(loan.id)

                        if subloan_response == 'success':
                            return JsonResponse({'message':'Payment Successful'},status = 200)
                        else:
                            return JsonResponse({'message':'Internal Server Error'},status = 500)
                    
                    return JsonResponse({'message':'Installments already paid'},status = 400)
                return JsonResponse({'message':'Unauthorized User'},status = 401)


                



            except Exception as e:
                return JsonResponse({'error':str(e)},status = 400)

