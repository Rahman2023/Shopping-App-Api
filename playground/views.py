from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from store.models import Product, OrderItem
# Create your views here.
def say_hello(request):

    return render(request, 'hello.html', {'name': 'Rahman'})