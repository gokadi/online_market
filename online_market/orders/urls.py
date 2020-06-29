from django.urls import path

from online_market.orders.views import make_order

app_name = 'orders'

urlpatterns = [
    path('make_order/', make_order, name='make_order'),
]
