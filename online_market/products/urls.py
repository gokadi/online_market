from django.urls import path

from online_market.products.views import catalog

app_name = 'products'

urlpatterns = [
    path('catalog/<int:category_pk>/', catalog, name='catalog_view'),
]
