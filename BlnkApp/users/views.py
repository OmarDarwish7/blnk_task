from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .models import UserModel
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from loan_provider.models import LoanProviderModel
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password

# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'POST':

        json_data = json.loads(request.body.decode('utf-8'))
        username = json_data.get('username')
        password = json_data.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user
            returned = {
                'id':user.id,
                'username':user.username,
                'user_type':user.user_type
            }
            return JsonResponse({'data':returned},status = 200)
        
        else: 
            return JsonResponse({'data':'No user found'}, status = 400)


@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        try:
            # json_data = json.loads(request.body.decode('utf-8'))

            json_data = json.loads(request.body.decode('utf-8'))

            # Extract username and password from JSON data
            username = json_data.get('username')
            password = json_data.get('password')
            user_type = json_data.get('user_type')
            phone_number = json_data.get('phone_number')
            national_id = json_data.get('national_id')
            date_of_birth = json_data.get('date_of_birth')

            # Create a new user with a hashed password
            user = UserModel.objects.create_user(
                username=username, 
                password=password,
                user_type = user_type,
                phone_number = phone_number,
                national_id = national_id,
                date_of_birth = date_of_birth
                )

            user_data = {
                'id': user.id,
                'username': user.username,
                'password':user.password,
                'user_type' : user_type,
                'phone_number' : phone_number,
                'national_id' : national_id,
                'date_of_birth' : date_of_birth
                # Add more user fields as needed
            }

            if user_type == 'loan_provider':
                loan_provider = LoanProviderModel(id= user,current_total_funds = 0)
                loan_provider.save()

            # elif user_type == 'loan_customer':


            return JsonResponse({'message': 'User created successfully', 'user': user_data})

            # new_object = UserModel(
            #     name = json_data.get('name')
            # )

            # new_object.save()

            # return JsonResponse({'message':'Object Created Successfully'})
        
        except Exception as e:
            return JsonResponse({'error':str(e)})