from django.contrib import admin
from .models import Cart, CartItem


# Carts
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'cart_user', 'cart_items', 'date_added')
    # list_display_links = ('thumbnail_tag', 'title',)
    # list_filter = ('publish', 'status')
    # search_fields = ('description', 'title')
    # prepopulated_fields = {'slug': ('title',)}
    # ordering = ['-status', '-publish']
    # actions = ['make_published', 'make_draft']
    # list_per_page = 25
admin.site.register(Cart, CartAdmin)

# Cart Items
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'user_of_cart', 'quantity', 'is_active')
    # list_display_links = ('thumbnail_tag', 'title',)
    # list_filter = ('publish', 'status')
    # search_fields = ('description', 'title')
    # prepopulated_fields = {'slug': ('title',)}
    # ordering = ['-status', '-publish']
    # actions = ['make_published', 'make_draft']
    # list_per_page = 25
admin.site.register(CartItem, CartItemAdmin)