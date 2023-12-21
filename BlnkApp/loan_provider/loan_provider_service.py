from .models import LoanProviderModel
from django.db.models import Sum
from django.forms import model_to_dict
from django.http import JsonResponse

def increase_total_funds(id,fund):

    try:
        print(id)
        print(fund)
        provider = LoanProviderModel.objects.get(pk=id)

        print(provider)

        provider.current_total_funds = provider.current_total_funds + fund

        provider.save()

        print(model_to_dict(provider))
    
    except Exception as e:
        return JsonResponse({'error':str(e)})
    
def decrease_total_funds(id,amount):
    # try:
        provider = LoanProviderModel.objects.get(pk=id)

        print(f"In decrease total funds {provider}")

        print(f'provider {provider.current_total_funds}')

        provider.current_total_funds -= amount

        print(f'current funds after : {provider.current_total_funds}')

        # provider.current_total_funds = provider.current_total_funds - float(amount)

        # print(f"in decrease 2 : {provider.current_total_funds}")

        provider.save()

        return 'success'
    
    # except Exception as e:
    #     return JsonResponse({'error':str(e)})
    
def get_total_budget():
    try:
        total_budget = LoanProviderModel.objects.aggregate(total=Sum('current_total_funds'))['total']

        if total_budget is not None:
            return total_budget
    except Exception as e:
        return str(e)
    
def get_shares():
    try:
        all_providers = LoanProviderModel.objects.all()

        if len(all_providers) > 0 :
            shares = []
            total_budget = get_total_budget()
            for provider in all_providers:
                if provider.current_total_funds > 0:
                    provider_share = provider.current_total_funds / total_budget
                    shares.append(
                        {
                            'id':provider,
                            'share': provider_share
                            }
                        )
            return shares
        else:
            return []
        
    except Exception as e:
        return str(e)