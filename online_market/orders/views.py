from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.db import transaction
from django.db.models import Sum
from django.http import HttpResponse
from django.template.response import TemplateResponse

from online_market.orders.models import Order, OrderProduct
from online_market.products.models import Product


def make_order(request: WSGIRequest) -> HttpResponse:
    cart = request.session.get(settings.CART_SESSION_ID, [])
    products = Product.objects.filter(pk__in=cart)
    products_in_cart = []
    total_price = 0
    for product in products:
        product_amount = cart.count(str(product.pk))
        products_in_cart.append([product, product_amount])
        total_price += product.price * product_amount
    if request.method == 'POST':
        with transaction.atomic():
            order = Order.objects.create(
                user=request.user,
                address=request.user.address,
                total_price=total_price,
                status=Order.STATUS_ACCEPTED
            )
            for product in products_in_cart:
                OrderProduct.objects.create(
                    order=order, product=product[0], amount=product[1]
                )

        request.session[settings.CART_SESSION_ID] = []
        request.session.modified = True
        return TemplateResponse(
            request,
            template='make_order.html',
            context={
                'page_title': 'Online Market | Order done',
                'is_order_successful': True,
            }
        )
    elif request.method == 'GET':
        return TemplateResponse(
            request,
            template='make_order.html',
            context={
                'products': products_in_cart,
                'total_price': total_price,
                'address': getattr(request.user, 'address', None),
                'page_title': 'Online Market | Finish order'
            }
        )
