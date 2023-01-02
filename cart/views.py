from django.shortcuts import render, redirect, get_object_or_404
from storefront.models import Product
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

# Create cart based on session id
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

@login_required
def add_cart(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) # Get the cart using the _cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()

    # For debug
    # return HttpResponse(f"<h1>{cart_item.product.title}</h1> \
    # <p>{str(cart_item.product.price)}</p> \
    # <p>{str(cart_item.quantity)}</p> \
    # <p>{str(cart_item.product.stock)}</p>")

    return redirect('cart:index')

@login_required
def subtract_cart(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    cart = Cart.objects.get(cart_id=_cart_id(request)) # Get the cart using the _cart_id present in the session
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1: 
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart:index')

@login_required
def remove_cart(request, product_pk):
    cart = Cart.objects.get(cart_id=_cart_id(request)) # Get the cart using the _cart_id present in the session
    product = get_object_or_404(Product, pk=product_pk)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()

    return redirect('cart:index')

@login_required
def clear_cart(request):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart.delete()

    return redirect('cart:index')

@login_required
def index(request, total=0, quantity=0, cart_items=None, cargo=100000, grand_total=0): #TODO put default cargo to 0 after calculate it
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
            # cargo += (cart_item.quantity * cargo_fee ) #TODO I should get user destination and weight of the product, then calc cargo fee for each product
        grand_total = total + cargo
    except:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cargo': cargo,
        'grand_total': grand_total,
        'cart_items': cart_items,
    }

    return render(request, 'cart/index.html', context)