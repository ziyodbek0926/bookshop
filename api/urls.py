from django.urls import path
from . import views


urlpatterns = [
    path('customers/', views.CustomerView.as_view()), # create, get all customers
    path('customers/<int:pk>/', views.CustomerDetailsView.as_view()), # get a customer, update, delete
    path('customers/<int:pk>/contact/', views.ContactView.as_view()),
]
