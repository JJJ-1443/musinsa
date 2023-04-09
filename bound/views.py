from django.shortcuts import render, redirect
from .models import BoundModel
from .models import ProductModel

def bound(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'bound.html')
        else:
            return redirect('/sign-in')

    elif request.method == 'POST':
        current_code = ProductModel.objects.get(code=code)
        user = request.user
        my_bound = BoundModel()
        my_bound.code = current_code
        my_bound.user = user
        my_bound.bound_price = request.POST.get('price', '')
        my_bound.save()
        return redirect('/bound')

