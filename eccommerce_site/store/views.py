from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    featured_products = Product.objects.filter(is_featured=True)
    return render(request, 'home.html', {'featured_products': featured_products})

def about(request):
    return render(request, 'about.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def contact(request):
    return render(request, 'contact.html')

def forum(request):
    return render(request, 'forum.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def account(request):
    return render(request, 'account.html')