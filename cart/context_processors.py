from .views import _cart_id
from .models import Cart, CartItem

def cart_info(request, quantity=0):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            quantity += cart_item.quantity
    except:
        pass


    context = {
        'cart_quantity': quantity
    }
    return context


