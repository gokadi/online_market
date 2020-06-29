from django.urls import path

from online_market.carts.views import cart_view, add_to_cart, remove_from_cart

app_name = 'carts'

urlpatterns = [
    path('cart/', cart_view, name='cart_view'),
    path('add_to_cart/', add_to_cart, name='add'),
    path('remove_from_cart/', remove_from_cart, name='remove'),
]
