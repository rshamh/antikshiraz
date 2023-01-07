from django.db import models
from storefront.models import Product


# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    cart_user = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def __str__(self):
        return self.cart_id

    def cart_items(self):
        items = CartItem.objects.filter(cart=self.pk)
        return [item for item in items]



class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'کالای سبد خرید'
        verbose_name_plural = 'کالاهای سبد های خرید'

    def __str__(self):
        return self.product.title

    @property
    def total_cost(self):
        return self.quantity * self.product.price

    def user_of_cart(self):
        return self.cart.cart_user
