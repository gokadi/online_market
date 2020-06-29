from django import template

from online_market.orders.models import OrderProduct, Order
from online_market.products.models import Product

register = template.Library()


@register.simple_tag
def get_product_amount_in_order(product_pk: int, order_pk: int) -> int:
    return OrderProduct.objects.get(product=product_pk, order=order_pk).amount
