from django import template
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse

from online_market.navigation import NavigationItem

register = template.Library()


@register.inclusion_tag('contrib/sidebar.html')
def profile_sidebar(request: WSGIRequest) -> dict:
    return {'items': (
        NavigationItem(
            label='Контакты', raw_url=reverse('users:profile_contacts'),
            is_active=request.path == reverse('users:profile_contacts')
        ),
        NavigationItem(
            label='Адрес', raw_url=reverse('users:profile_address'),
            is_active=request.path == reverse('users:profile_address')
        ),
        NavigationItem(
            label='Заказы', raw_url=reverse('users:orders'),
            is_active=request.path == reverse('users:orders')
        ),
    )}
