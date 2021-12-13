from django.contrib import admin
from .models import Category, Product, CartProduct, Cart, Customer, Specifications


class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


class CartProductAdmin(admin.ModelAdmin):
    pass


class CartAdmin(admin.ModelAdmin):
    pass


class CustomerAdmin(admin.ModelAdmin):
    pass


class SpecificationsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartProduct, CartProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Specifications, SpecificationsAdmin)





