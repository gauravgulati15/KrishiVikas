from django.shortcuts import render
from products.models import Product
# Create your views here.


def home(request):
    products = Product.objects.filter(is_new=True).order_by('-id')[:9]

    context = {
        'products': products,
    }

    return render(request, "home/index.html", context)
