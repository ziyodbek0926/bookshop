from django.views import View
from django.http import HttpRequest, JsonResponse


class CustomersView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        # TODO: get all customers
        pass

    def post(self, request: HttpRequest) -> JsonResponse:
        # TODO: create a new customer
        pass


class CustomerDetailsView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        # TODO: get customer
        pass

    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        # TODO: udpate customer
        pass

    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        # TODO: delte customer
        pass


class ContactView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        # TODO: get contact
        pass

    def post(self, request: HttpRequest, pk: int) -> JsonResponse:
        # TODO: create contact
        pass

    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        # TODO: udpate contact
        pass

    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        # TODO: delte contact
        pass
