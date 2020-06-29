from django import template
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse

from online_market.navigation import NavigationItem

register = template.Library()


@register.inclusion_tag('contrib/header.html')
def header(request: WSGIRequest):
    header_links = (
        NavigationItem(
            raw_url=reverse('index'), label='Главная страница',
            is_active=request.path == reverse('index')
        ),
        NavigationItem(
            raw_url=reverse('delivery'), label='Оплата и доставка',
            is_active=request.path == reverse('delivery')
        ),
        NavigationItem(
            raw_url=reverse('about'), label='О нас',
            is_active=request.path == reverse('about')
        ),
    )

    return {
        'items': header_links,
        'user': request.user,
    }
