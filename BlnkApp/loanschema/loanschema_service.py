from .models import LoanSchemaModel
from django.forms import model_to_dict

def get_loan_schema(amount):
    try:
        all_schemas = LoanSchemaModel.objects.all()

        if len(all_schemas) >0:
            for schema in all_schemas:
                if amount >= schema.min_amount and amount <= schema.max_amount:
                    return model_to_dict(schema)
        return "404"    

    except Exception as e:
        return "404"