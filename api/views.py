from django.views import View
from django.http import HttpRequest, JsonResponse
from .models import Customer, Contact, Publisher, Language, Book
from django.forms import model_to_dict
import json
from django.core.exceptions import ObjectDoesNotExist


class CustomersView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        """get all customers

        Args:
            request (HttpRequest): _description_

        Returns:
            JsonResponse: _description_
        """
        result = []
        for customer in Customer.objects.all():
            result.append(model_to_dict(customer, fields=['id', 'first_name', 'last_name', 'username']))

        return JsonResponse(result, safe=False)

    def post(self, request: HttpRequest) -> JsonResponse:
        """create a new customer

        Args:
            request (HttpRequest): _description_

        Returns:
            JsonResponse: _description_
        """
        data = json.loads(request.body.decode())

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        if all([first_name, last_name, username, password]):
            Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password
            )

            return JsonResponse({'message': 'object created.'}, status=201)

        else:
            return JsonResponse({'error': 'invalid data.'}, status=404)


class CustomerDetailsView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        """get customer

        Args:
            request (HttpRequest): _description_
            pk (int): _description_

        Returns:
            JsonResponse: _description_
        """
        try:
            customer = Customer.objects.get(id=pk)
        except (ObjectDoesNotExist, Customer.DoesNotExist):
            return JsonResponse({'error': 'customer does not exist.'}, status=404)
        
        result = model_to_dict(customer, fields=['id', 'first_name', 'last_name', 'username'])
        return JsonResponse(result)

    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        """udpate customer

        Args:
            request (HttpRequest): _description_
            pk (int): _description_

        Returns:
            JsonResponse: _description_
        """
        try:
            customer = Customer.objects.get(id=pk)
        except (ObjectDoesNotExist, Customer.DoesNotExist):
            return JsonResponse({'error': 'customer does not exist.'}, status=404)

        data = json.loads(request.body.decode())

        customer.first_name = data.get('first_name', customer.first_name)
        customer.last_name = data.get('last_name', customer.last_name)
        customer.username = data.get('username', customer.username)
        customer.password = data.get('password', customer.password)

        customer.save()

        return JsonResponse({'message': 'customer updated.'}, status=203)

    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        """delte customer

        Args:
            request (HttpRequest): _description_
            pk (int): _description_

        Returns:
            JsonResponse: _description_
        """        
        try:
            customer = Customer.objects.get(id=pk)
        except (ObjectDoesNotExist, Customer.DoesNotExist):
            return JsonResponse({'error': 'customer does not exist.'}, status=404)

        customer.delete()

        return JsonResponse({'message': 'customer deleted.'}, status=204)


class ContactView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        try:
            customer = Customer.objects.get(id=pk)
        except (ObjectDoesNotExist, Customer.DoesNotExist):
            return JsonResponse({'error': 'customer does not exist.'}, status=404)
        
        try:
            contact = Contact.objects.get(customer=customer)
        except (ObjectDoesNotExist, Contact.DoesNotExist):
            return JsonResponse({'error': 'contact does not exist.'}, status=404)

        result = model_to_dict(contact)

        return JsonResponse(result)

    def post(self, request: HttpRequest, pk: int) -> JsonResponse:
        """create contact

        Args:
            request (HttpRequest): _description_
            pk (int): _description_

        Returns:
            JsonResponse: _description_
        """ 
        try:
            customer = Customer.objects.get(id=pk)
        except (ObjectDoesNotExist, Customer.DoesNotExist):
            return JsonResponse({'error': 'customer does not exist.'}, status=404)

        data = json.loads(request.body.decode())   

        Contact.objects.create(
            customer=customer,
            email=data['email'],
            address=data['address'],
            phone=data['phone'],
        )

        return JsonResponse({'message': 'object created.'}, status=201) 

    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        # TODO: udpate contact
        pass

    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        # TODO: delte contact
        pass


class PublishersView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        pass
    
    def post(self, request: HttpRequest) -> JsonResponse:
        pass
    

class PublisherDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass


class LanguagesView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        pass
    
    def post(self, request: HttpRequest) -> JsonResponse:
        pass
    

class LanguageDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass


class BooksView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        params = request.GET

        if params.get('title', False):
            books = Book.objects.filter(title__icontains=params.get('title'))
        elif params.get('description', False):
            books = Book.objects.filter(description__icontains=params.get('description'))
        elif params.get('price', False):
            books = Book.objects.filter(price__lte=params.get('price'))
        elif params.get('lang', False):
            books = Book.objects.filter(lang__lang__icontains=params.get('lang'))
        elif params.get('publisher', False):
            books = Book.objects.filter(publisher__name__icontains=params.get('publisher'))
        else:
            books = Book.objects.all()

        result = [model_to_dict(book) for book in books]
        return JsonResponse(result, safe=False)
         
    def post(self, request: HttpRequest) -> JsonResponse:
        pass
    

class BookDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    