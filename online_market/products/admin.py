from typing import Tuple

from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet, Q

from online_market.products.forms import CategoryForm
from online_market.products.models import Product, Category


class NestedCategoriesFilter(admin.SimpleListFilter):
    title = 'Categories'
    parameter_name = 'category'

    def lookups(
        self, request: WSGIRequest, model_admin: admin.ModelAdmin
    ) -> Tuple[Tuple[str, str], ...]:
        return tuple(
            (str(category), str(category).capitalize())
            for category in Category.objects.all()
        )

    def queryset(self, request: WSGIRequest, queryset: QuerySet) -> QuerySet:
        value_to_filter_by = self.value()
        if value_to_filter_by:
            return queryset.filter(
                Q(category__name=value_to_filter_by)
                | Q(category__parent_category__name=value_to_filter_by)
            )
        else:
            return queryset


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm

    list_display = ('name', 'parent_category', )
    list_filter = ('parent_category', )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category', 'available_amount',
        'price_with_currency', 'is_active',
    )
    list_filter = (NestedCategoriesFilter, 'is_active', )
    list_editable = ('category', 'available_amount', 'is_active', )

    def price_with_currency(self, obj: Product) -> str:
        return f'{obj.price} ₽'

    price_with_currency.short_description = 'Price'  # type: ignore

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['category'].queryset = Category.objects.filter(
            subcategories__isnull=True
        )
        return form


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
