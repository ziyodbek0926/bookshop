from django.urls import path
from . import views


urlpatterns = [
    path('customers/', views.CustomersView.as_view()), # create, get all
    path('customers/<int:pk>/', views.CustomerDetailsView.as_view()), # get, update, delete
    path('customers/<int:pk>/contact/', views.ContactView.as_view()), # get, update, delete, create
]
