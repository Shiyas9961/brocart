from django import template

register = template.Library()

@register.simple_tag(name="order_status")
def order_status (status) :

    status = int(status)
    if status == 1:
        return "Confirmed"
    elif status == 2:
        return "Proccessing"
    elif status == 3:
        return "Deliverd"
    else :
        return "Rejected"