from django.db import models
from storefront.models import Product


# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'کالای سبد خرید'
        verbose_name_plural = 'کالاهای سبد های خرید'

    def __str__(self):
        return self.product + '-' + self.cart

    @property
    def total_cost(self):
        return self.quantity * self.product.price
