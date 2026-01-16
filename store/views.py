# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    # Get first 8 products as featured
    products = Product.objects.all()[:8]

    # Calculate discount percent for products
    for p in products:
        if p.discount_price:
            p.discount_percent = round((p.price - p.discount_price) / p.price * 100)
        else:
            p.discount_percent = 0

    return render(request, 'store/home.html', {'products': products})


def product_list(request):
    q = request.GET.get('q')
    if q:
        products = Product.objects.filter(title__icontains=q)
    else:
        products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product': product})


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login(request, user)
        messages.success(request, "Account created successfully")
        return redirect('product_list') 

    return render(request, 'store/signup.html')

@login_required
def cart(request):
    return render(request, 'store/cart.html')

@login_required
def checkout(request):
    return render(request, 'store/checkout.html')

@login_required
def profile(request):
    return render(request, 'store/profile.html')

@login_required
def orders(request):
    return render(request, 'store/orders.html')

def contact(request): return render(request, 'store/contact.html')
def about(request): return render(request, 'store/about.html')
