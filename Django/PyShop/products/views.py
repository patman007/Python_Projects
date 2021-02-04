from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# /products -> index
#Uniform Resource Locator
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                {'products': products})
    # return HttpResponse('Hello World')

def new(request):
    return HttpResponse('New Products')



#Use the words in the cmd prompt window in Pyshop address not second one
#python manage.py runserver
#127.0.0.1:8000 is the address to start server in chrom address bar

