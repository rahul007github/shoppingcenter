from django.contrib import admin
from .models import *



admin.site.register(Category)
admin.site.register(Coupon)

class ProductImageAdmin(admin.StackedInline):
    model=ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','price']
    inlines=[ProductImageAdmin]

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display=['color_name','price']
    model= ColorVariant

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display=['size_name','price']
    model= SizeVariant

@admin.register(Quantity)
class QuantityAdmin(admin.ModelAdmin):
    list_display=['product_quantity','price']
    model= Quantity

admin.site.register(Product,ProductAdmin)

admin.site.register(ProductImage)
