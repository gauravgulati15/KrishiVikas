from django.shortcuts import redirect, render
from .models import *
from django import http
from .forms import CommentForm
from django.db.models import Q

# Create your views here.


def product_list(request):
    product_list = Product.objects.all()

    search_query = request.GET.get('q')
    if search_query:
        product_list = product_list.filter(
            Q(name__icontains=search_query)
            | Q(category__name__icontains=search_query)
            | Q(vendor__name__icontains=search_query)).distinct()

    categories = Category.objects.all()

    context = {'product_list': product_list, 'categories': categories}

    return render(request, 'product/product_list.html', context)


def product_detail(request, id):
    product_detail = Product.objects.get(id=id)
    categories = Category.objects.all()

    comments = ProductComment.objects.filter(product=product_detail)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.product = product_detail
            comment.save()
            return redirect('products:product_detail', id=id)
    else:
        comment_form = CommentForm()

    context = {
        'product': product_detail,
        'categories': categories,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'product/product_detail.html', context)


def product_by_category(request, cat):
    product_by_category = Product.objects.filter(category__name=cat)
    categories = Category.objects.all()

    context = {'product_list': product_by_category, 'categories': categories}
    return render(request, 'product/product_list.html', context)
