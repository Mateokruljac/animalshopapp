from members.models import Order


def cart_total_quantity(request):
    if request.user.is_authenticated:
        customer = request.user.customer #one to one relationship
        order,created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all() 
        cart_items = order.get_total_items
    else:
        items = []
        order = []
        cart_items = 0
    
    context = {"order":order,"items":items,"cart_items":cart_items}
    
    return context