from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.template.response import TemplateResponse

from online_market.products.models import Product


def cart_view(request: WSGIRequest) -> HttpResponse:
    if request.method == 'GET':
        cart = request.session.get(settings.CART_SESSION_ID, [])
        products_in_cart = []
        for product in Product.objects.filter(pk__in=cart):
            products_in_cart.extend(
                [product for _ in range(cart.count(str(product.pk)))]
            )
        return TemplateResponse(
            request, template='cart.html', context={
                'products': products_in_cart,
                'page_title': 'Online Market | Cart'
            }
        )


def add_to_cart(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        cart = request.session.get(settings.CART_SESSION_ID, [])
        cart.append(request.POST.get('product_id'))
        request.session.modified = True

    return HttpResponse(status=201)


def remove_from_cart(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        cart = request.session.get(settings.CART_SESSION_ID, [])
        if cart:
            cart.remove(request.POST.get('product_id'))
        request.session.modified = True
        return HttpResponse(status=201)
