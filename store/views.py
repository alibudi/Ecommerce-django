from django.shortcuts import render

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def cart(request):
    context = {}
    return  render(request, 'store/cart.html', context)

def store(request):
    context = {}
    return render(request, 'store/store.html', context)
# Create your views here.
