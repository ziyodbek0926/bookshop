from django.contrib import admin
from .models import Customer, Contact, Publisher, Language, Book

all_models = (Customer, Contact, Publisher, Language, Book)

admin.site.register(all_models)