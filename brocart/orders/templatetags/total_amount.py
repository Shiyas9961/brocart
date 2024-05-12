from django import template

register = template.Library()

@register.simple_tag(name='total_amount')
def total_amout (cart) :
    
    total = 0
    for cart_item in cart.order_details.all() :
        total += cart_item.quantity * cart_item.product.price

    return total