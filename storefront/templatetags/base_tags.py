from django import template
from ..models import SiteInfo, NavBar, Category, SlideShow

register = template.Library()

@register.simple_tag
def title():
    return SiteInfo.objects.get(position=1).title

@register.simple_tag
def logo():
    return SiteInfo.objects.get(position=1).thumbnail.url

@register.inclusion_tag('storefront/slideshow.html')
def slideshow():
    return {
        'slideshow' : SlideShow.objects.all()
    }

@register.inclusion_tag('storefront/navbar.html')
def navbar():
    return {
        'navbar' : NavBar.objects.filter(status=True),
        'category': Category.objects.filter(status=True).order_by('position')
    }  

@register.filter
def persian_number(my_str):
    numbers = {
        "0" : "۰",
        "1" : "۱",
        "2" : "۲",
        "3" : "۳",
        "4" : "۴",
        "5" : "۵",
        "6" : "۶",
        "7" : "۷",
        "8" : "۸",
        "9" : "۹",
    }
    my_str = str(my_str)
    for e, p in numbers.items():
        my_str = my_str.replace(e, p)
    
    return my_str

@register.filter
def persian_intcomma(value):
        str_value = str(value)[::-1]
        new_value = ''
        for i in range(len(str_value)):
            new_value += str_value[i]
            if (i+1) % 3 == 0 and i != len(str_value) - 1:
                new_value += ','
        return new_value[::-1]