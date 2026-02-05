from django.contrib import admin
from restaurant_app.models import Table,MenuCategory,MenuItem,Order,OrderItem,Bill

# Register your models here.

admin.site.register(Table)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Bill)
