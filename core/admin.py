from django.contrib import admin
from .models import Customer, Product, OrderPlaced, Cart, Banners
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ('user', 'customer', 'product', 'quantity', 'ordered_date', 'status')

admin.site.register(OrderPlaced, OrderPlacedAdmin)


admin.site.register(Customer)
admin.site.register(Product)
# admin.site.register(OrderPlaced)
admin.site.register(Cart)
admin.site.register(Banners)

