from django.apps import apps
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from online_market import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(
        template_name='index.html',
        extra_context={'page_title': 'Online Market'}
    ), name='index'),
    path('about/', TemplateView.as_view(
        template_name='about.html',
        extra_context={'page_title': 'Online Market | About us'}
    ), name='about'),
    path('delivery/', TemplateView.as_view(
        template_name='delivery.html',
        extra_context={'page_title': 'Online Market | About us'}
    ), name='delivery'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


if apps.is_installed('online_market.users'):
    urlpatterns += [
        path(
            'users/',
            include('online_market.users.urls', namespace='users')
        )
    ]

if apps.is_installed('online_market.orders'):
    urlpatterns += [
        path(
            'orders/',
            include('online_market.orders.urls', namespace='orders')
        )
    ]

if apps.is_installed('online_market.products'):
    urlpatterns += [
        path(
            'products/',
            include('online_market.products.urls', namespace='products')
        )
    ]

if apps.is_installed('online_market.carts'):
    urlpatterns += [
        path(
            'products/',
            include('online_market.carts.urls', namespace='carts')
        )
    ]
