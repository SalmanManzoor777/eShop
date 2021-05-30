from django.shortcuts import render, redirect

# Create your views here.


def index(request):
	return render(request, 'index-cosmetics.html')

def category(request):
	return render(request, 'category-closed.html')


def product(request):
	return render(request, 'product.html')


def cart(request):
	return render(request, 'cart.html')


def checkout(request):
	return render(request, 'checkout.html')


def men(request):
	return render(request, 'category-men.html')


def women(request):
	return render(request, 'category-women.html')


def account(request):
	return render(request, 'account.html')
