from django.shortcuts import render, redirect
from products.models import Product
from .models import Order, OrderItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def cart_page (request) :
    user = request.user
    customer = user.customer_profile
    cart_items, created = Order.objects.get_or_create(
        owner = customer,
        order_status = Order.CART_STAGE
    )
    context = {
        'cart' : cart_items
    }
    return render(request, 'orders/cart.html', context)


@login_required(login_url='account')
def remove_from_cart (request, id) :
    item = OrderItem.objects.get(id = id)

    if item :
        item.delete()
    
    return redirect('cart')

@login_required(login_url='account')
def add_to_cart (request) :
    if request.POST :
        user = request.user
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        customer = user.customer_profile
        product = Product.objects.get(id = product_id)

        cart_obj, created = Order.objects.get_or_create(
            owner = customer,
            order_status = Order.CART_STAGE
        )

        order_item, created = OrderItem.objects.get_or_create(
            product = product,
            owner = cart_obj
        )

        if created :
            order_item.quantity = quantity
            order_item.save()
        else :
            order_item.quantity = order_item.quantity + quantity
            order_item.save()
        return redirect('cart')
    
@login_required(login_url='account')    
def checkout_order (request) :
    if request.POST:

        try:
            total = float(request.POST.get('total'))
            user = request.user
            customer = user.customer_profile

            order_obj = Order.objects.get(
                owner = customer,
                order_status = Order.CART_STAGE
            )

            if order_obj:
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.total_price = total
                order_obj.save()
                status_msg = "Your Order successfully registerd, Order will be delivered within few days"
                messages.success(request, status_msg)
            else:
                status_msg = "Your cart items is'nt exist or Something went wrong"
                messages.error(request, status_msg)

        except Exception as e:
                status_msg = "Your cart items is'nt exist or Something went wrong"
                messages.error(request, status_msg)
    
    return redirect('cart')

def view_orders (request) :

    user = request.user
    customer = user.customer_profile
    all_orders = Order.objects.filter(owner = customer).exclude(order_status = Order.CART_STAGE)
    context = {'orders' : all_orders}
    
    return render(request, 'orders/orders.html', context)