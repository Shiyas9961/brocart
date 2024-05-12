from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.

def home (request) :
    latest_products = Product.objects.order_by('-id')[:4]
    featured_products = Product.objects.order_by('priority')[:4]

    context = {
        'latest_products' : latest_products,
        'featured_products' : featured_products
    }

    return render(request, 'home/index.html', context)

def products (request) :
    page = 1

    if request.GET :
        page = request.GET.get('page', 1)

    prod_list = Product.objects.order_by('priority')

    paginator_obj = Paginator(prod_list, 4)
    prod_list = paginator_obj.get_page(page)
    context = { 'products' : prod_list }

    return render(request, 'product/all_product.html', context)

def single_product (request, id) :
    product = Product.objects.get( id = id)

    context = { 'product' : product }
    return render(request, 'product/single_product.html', context)