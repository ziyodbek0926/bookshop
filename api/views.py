from django.views import View
from django.http import HttpRequest, JsonResponse
from .models import Contact, Customer
from django.forms import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
import json


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
        # TODO: create post view  
        pass     


class CustomerDetailsView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass

    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass

    def patch(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass

    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass


class ContactView(View):
    def get(self, reqeust: HttpRequest, pk: int) -> JsonResponse:
        try:
            customer = Customer.objects.get(id=pk)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'customer does not exist.'})

        try:
            contact = Contact.objects.get(customer=customer)
        except (ObjectDoesNotExist, contact.DoesNotExist):
            return JsonResponse({'error': 'contact does not exist.'})
        

        result = model_to_dict(contact)
        return JsonResponse(result)

    def post(self, reqeust: HttpRequest, pk: int) -> JsonResponse:
        try:
            customer = Customer.objects.get(id=pk)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'customer does not exist.'})

        data = json.loads(reqeust.body.decode())

        contact = Contact.objects.create(
            customer=customer, 
            email=data.get('email'),
            address=data.get('address'),
            phone=data.get('phone')
        )

        result = model_to_dict(contact)
        return JsonResponse(result, status=201)

    def put(self, reqeust: HttpRequest) -> JsonResponse:
        pass

    def delete(self, reqeust: HttpRequest) -> JsonResponse:
        pass 
