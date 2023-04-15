from django.db import models
from django.utils import timezone
from Extensions.utils import jalali_converter, persian_number_conv
from django.utils.html import format_html
from django.urls import reverse


# Managers:
# class PublishedManager(models.Manager):
#     def published(self):
#         return self.filter(status=True)

# Models:
class SiteInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان سایت')
    thumbnail = models.ImageField(upload_to='site', verbose_name='عکس')
    position = models.IntegerField(unique=True, verbose_name='موقعیت')

    class Meta:
        verbose_name = 'اطلاعات سایت'
        verbose_name_plural = 'اطلاعات سایت'
        ordering = ['position']

    def __str__(self):
        return self.title


class NavBar(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(max_length=30, unique=True, blank=True, verbose_name='آدرس')
    status = models.BooleanField(default=True, verbose_name='وضعیت انتشار')
    position = models.IntegerField(unique=True, verbose_name='موقعیت')
    
    class Meta:
        verbose_name = 'منو'
        verbose_name_plural = 'منو ها'
        ordering = ['position']

    def __str__(self):
        return self.title


class SlideShow(models.Model):
    title = models.CharField(max_length=300,null=True , verbose_name='عنوان اسلاید')
    description = models.TextField(null=True, verbose_name='توضیحات')
    image = models.ImageField(upload_to='slideshow', verbose_name='عکس')
    position = models.IntegerField(unique=True, verbose_name='موقعیت')

    class Meta:
        verbose_name = 'اسلاید شو'
        verbose_name_plural = 'اسلاید شو'
        ordering = ['position']

    def __str__(self):
        return self.title


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name='زیردسته')
    title = models.CharField(max_length=100, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=30, unique=True, verbose_name='آدرس دسته بندی', allow_unicode = True)
    status = models.BooleanField(default=True, verbose_name='وضعیت انتشار')
    position = models.IntegerField(verbose_name='موقعیت')
    

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title

    # obejcts = PublishedManager()

class Product(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده')
    )

    title = models.CharField(max_length=100, verbose_name='عنوان محصول')
    slug = models.SlugField(max_length=30, unique=True, verbose_name='آدرس محصول', allow_unicode = True)
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', name='category', related_name='products')
    description = models.TextField(verbose_name='توضیحات')
    thumbnail = models.ImageField(upload_to='images', verbose_name='عکس')
    price = models.DecimalField(max_digits=7, decimal_places=0, verbose_name='قیمت')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stock = models.IntegerField(default=1, verbose_name='تعداد موجود')
    status = models.BooleanField(default=True, verbose_name='وضعیت انتشار')

    
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ['-publish']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("shopadmin:products")
    

    def jpublish(self):
        '''Convert Gorgian date format to Jalali'''
        return jalali_converter(self.publish)
    jpublish.short_description = 'زمان انتشار'
    
    
    def p_title(self):
        '''Convert numbers in title to persian characters'''
        return persian_number_conv(str(self.title))

    def p_price(self):
        '''separate price by , for each thousands then convert it to persian characters'''
        str_price = str(self.price)[::-1]
        new_price = ''
        for i in range(len(str_price)):
            new_price += str_price[i]
            if (i+1) % 3 == 0 and i != len(str_price) - 1:
                new_price += ','
        new_price = new_price[::-1]
        return persian_number_conv(new_price)

    def thumbnail_tag(self):
        '''Adding thumbnail photo into the admin panel as a HTML format'''
        return format_html(f"<img width=60px height=60px style='border-radius: 5px;' src='{self.thumbnail.url}'")
    thumbnail_tag.short_description = 'عکس'

    def is_available(self):
        '''Check if that product available or not'''
        if self.stock > 0:
            return True
        else:
            return False
    is_available.boolean = True
    is_available.short_description = 'موجودی'
    
    # obejcts = PublishedManager()

    # @property
    # def category(self):
    #     return self.category.filter(status=True)

    # def category_published(self):
    #     return self.category.filter(status=True)
