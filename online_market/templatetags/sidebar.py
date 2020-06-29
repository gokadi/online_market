from django import template
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse

from online_market.navigation import NavigationItem
from online_market.products.models import Category

register = template.Library()


@register.inclusion_tag('contrib/sidebar.html')
def sidebar(request: WSGIRequest) -> dict:
    nav_items = []
    for category in Category.objects.all():
        is_any_subcategory_active = False
        if category.subcategories.exists():
            nested_items = []
            for subcategory in category.subcategories.all():
                if request.path.split('/')[-2] == str(subcategory.pk):
                    is_item_active = True
                    is_any_subcategory_active = True
                else:
                    is_item_active = False
                nested_items.append(
                    NavigationItem(
                        label=subcategory.name,
                        raw_url=reverse(
                            'products:catalog_view', args=[subcategory.pk]
                        ),
                        is_active=is_item_active
                    )
                )
            nav_items.append(NavigationItem(
                label=category.name,
                raw_url=reverse('products:catalog_view', args=[category.pk]),
                items=nested_items,
                is_active=is_any_subcategory_active
            ))
        elif not category.parent_category:
            nav_items.append(NavigationItem(
                label=category.name,
                raw_url=reverse('products:catalog_view', args=[category.pk]),
                is_active=request.path.split('/')[-2] == str(category.pk)
            ))

    return {'items': nav_items}
