from django.db import models
from customers.models import Customer
from products.models import Product


# Order Models

class Order (models.Model) :
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE, "Live"), (DELETE, "Delete"))

    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4

    ORDER_CHOICE = ( 
        ( ORDER_PROCCESSED, 'Order_Proccesed' ), 
        ( ORDER_DELIVERED, 'Order_Delivered' ), 
        ( ORDER_REJECTED, 'Order_Rejected' ) 
        )

    order_status = models.IntegerField(choices = ORDER_CHOICE, default = CART_STAGE)
    total_price = models.FloatField(null=True)
    owner = models.ForeignKey(Customer, on_delete = models.SET_NULL, related_name = 'user_order', null = True)
    delete_status = models.IntegerField(choices = DELETE_CHOICE, default = LIVE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.owner.name



class OrderItem (models.Model) :

    product = models.ForeignKey(Product, on_delete = models.SET_NULL, related_name = 'added_item', null = True)
    quantity = models.IntegerField(default = 1)
    owner = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = 'order_details')

    def __str__(self) -> str:
        return self.product.title