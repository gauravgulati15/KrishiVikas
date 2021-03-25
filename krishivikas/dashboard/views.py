from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

# FLASH MESSAGE
from django.contrib import messages

# for restricting dashboard access to non-logged in user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .forms import CreateUserForm, CustomerForm
from .decorators import unauthenticated_user, allowed_users, admin_only
from products.models import Product, Vendor, Customer

# Create your views here.


@login_required(login_url='accounts:login')
# @admin_only
def show_detail(request, id):
    product = Product.objects.get(id=id)
    vendor = Vendor.objects.get(name=product.vendor)
    products = Product.objects.all().filter(vendor=product.vendor)
    context = {
        'vendor': vendor,
        'products': products,
    }
    return render(request, "dashboard/showDetail.html", context)
