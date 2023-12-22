from django.forms import model_to_dict
from .models import SubloanModel

def create_subloan(subloan_object):

    print(subloan_object)

    try:
        if subloan_object is not None:
            subloan = SubloanModel(
                    share_of_total = subloan_object.get('share_of_total'),
                    monthly_amount = subloan_object.get('monthly_amount'),
                    total_amount = subloan_object.get('total_amount'),
                    current_paid = 0.0,
                    amount_to_pay = subloan_object.get('total_amount'),
                    loan = subloan_object.get('loan') ,
                    customer = subloan_object.get('customer'),
                    provider = subloan_object.get('provider') 
                )
            subloan.save()


            return 'success'

    except Exception as e:
        return str(e)
    
def pay_installments(loan_id):
    try:
        subloans = SubloanModel.objects.filter(loan_id = loan_id)

        if len(subloans) > 0:
            for subloan in subloans:
                subloan.current_paid += subloan.monthly_amount
                subloan.amount_to_pay -= subloan.monthly_amount
                if subloan.amount_to_pay <=0:
                    subloan.amount_to_pay = 0
                    subloan.current_paid = subloan.total_amount
               
                subloan.save()
            

            return 'success'
        return 'unsuccessful'

    except Exception as e:
        return 'unsuccessful'
