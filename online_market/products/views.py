from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse

from online_market.products.models import Product


def catalog(request: WSGIRequest, *args, **kwargs) -> TemplateResponse:
    if request.method == 'GET':
        category_pk = kwargs.get('category_pk', None)
        if category_pk is None:
            return redirect(reverse('index'))

        return TemplateResponse(
            request, template='catalog.html',
            context={
                'products': Product.objects.filter(category=category_pk),
                'page_title': 'Online Market | Catalog'
            }
        )
