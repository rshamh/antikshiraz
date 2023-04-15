from django.contrib import admin, messages
from .models import Product, Category, SiteInfo, SlideShow, NavBar
from django.utils.translation import ngettext



# Products
class ProductAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_tag', 'title', 'slug', 'jpublish', 'status', 'is_available', 'stock', 'category_to_str')
    list_display_links = ('thumbnail_tag', 'title',)
    list_filter = ('publish', 'status')
    search_fields = ('description', 'title')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']
    actions = ['make_published', 'make_draft']
    list_per_page = 25

    def category_to_str(self, obj):
            '''return all categories blong to that product'''
            return '، '.join(category.title for category in obj.category.all())
    category_to_str.short_description = 'دسته بندی'

    # Actions:
    @admin.action(description='انتشار محصولات انتخاب شده')
    def make_published(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
                f'{updated} عدد محصول با موقیت منتشر شد',
                f'{updated} عدد محصول با موقیت منتشر شدند',
                updated,
            ) , messages.SUCCESS)

    @admin.action(description='عدم انتشار محصولات انتخاب شده')
    def make_draft(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, ngettext(
                f'{updated} عدد محصول با موقیت از وضعیت انتشار خارج گردید',
                f'{updated} عدد محصول با موقیت از وضعیت انتشار خارج گردیدند',
                updated,
            ) , messages.SUCCESS)

admin.site.register(Product, ProductAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'parent', 'slug', 'status')
    list_display_links = ('title',)
    list_filter = (['status'])
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ['make_published', 'make_draft']

    # Actions:
    @admin.action(description='انتشار دسته بندی انتخاب شده')
    def make_published(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
                f'{updated} عدد دسته بندی با موقیت منتشر شد',
                f'{updated} عدد دسته بندی با موقیت منتشر شدند',
                updated,
            ) , messages.SUCCESS)

    @admin.action(description='عدم انتشار دسته بندی انتخاب شده')
    def make_draft(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, ngettext(
                f'{updated} عدد دسته بندی با موقیت از وضعیت انتشار خارج گردید',
                f'{updated} عدد دسته بندی با موقیت از وضعیت انتشار خارج گردیدند',
                updated,
            ) , messages.SUCCESS)

admin.site.register(Category, CategoryAdmin)



# Site Settings
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('position', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)

admin.site.register(SiteInfo, SiteInfoAdmin)


class SlideShowAdmin(admin.ModelAdmin):
    list_display = ('position', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)

admin.site.register(SlideShow, SlideShowAdmin)


class NavBarAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_display_links = ('title',)
    search_fields = ('title',)

admin.site.register(NavBar, NavBarAdmin)


