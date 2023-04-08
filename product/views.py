from django.shortcuts import render, redirect
from .models import ProductModel

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/product')
    else:
        return redirect('/sign-in')


def product(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'product.html')
        else:
            return redirect('/sign-in')
    elif request.method == 'POST':
        user = request.user
        my_product = ProductModel()
        my_product.seller = user
        my_product.code = request.POST.get('code', '')
        my_product.prod_name = request.POST.get('prod_name', '')
        my_product.desc = request.POST.get('desc', '')
        my_product.price = request.POST.get('price', '')
        my_product.sizes = request.POST.get('sizes', '')
        my_product.save()
        return render(request, 'product.html')


