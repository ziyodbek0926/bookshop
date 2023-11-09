from django.views import View
from django.http import HttpRequest, JsonResponse
from .models import Contact, Customer
from django.forms import model_to_dict


class CustomerView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        """get all custmers

        Args:
            request (HttpRequest): _description_

        Returns:
            JsonResponse: _description_
        """
        results = []
        for customer in Customer.objects.all():
            results.append(model_to_dict(customer, fields=['id', 'first_name', 'last_name', 'username']))

        return JsonResponse(results, safe=False)

    def post(self, request: HttpRequest) -> JsonResponse:
        """create customer

        Args:
            request (HttpRequest): _description_

        Returns:
            JsonResponse: _description_
        """   
        pass     



class CustomerDetailsView(View):
    pass


class ContactView(View):
    pass


class ContactDetailsView(View):
    pass

