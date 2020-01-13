from django.contrib import admin
# from django.contrib.contenttypes.admin import TabularInline

from .models import Product, Phone, Accessory, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class PhoneAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline
    ]


class AccessoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline
    ]


admin.site.register(Product)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Accessory, AccessoryAdmin)
