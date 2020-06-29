from django.contrib import admin

from online_market.orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'address', 'total_price', 'status', 'date_created',
    )


admin.site.register(Order, OrderAdmin)
