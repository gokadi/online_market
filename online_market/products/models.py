from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True, related_name='subcategories'
    )

    objects = models.Manager()

    def clean(self):
        if self.parent_category == self:
            raise ValidationError('A category cannot be its own subcategory.')

        if self.subcategories.exists() and self.parent_category:
            raise ValidationError('Parent category cannot have parent.')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products_images', blank=True)
    available_amount = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def clean(self):
        if self.category.subcategories.exists():
            raise ValidationError('A category cannot be parent category.')

    class Meta:
        ordering = ('name', )
        verbose_name = 'product'
        verbose_name_plural = 'products'
