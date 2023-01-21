from user_shop.models import product
from django.shortcuts import render


def sort_low_to_high(request):
    products = product.objects.all().order_by('price')
    return render(request, 'sort_low_to_high.html', {'products': products})

def sort_high_to_low(request):
    products = product.objects.all().order_by('-price')
    return render(request, 'sort_high_to_low.html', {'products': products})