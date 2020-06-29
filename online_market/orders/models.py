from django.conf import settings
from django.db import models

from online_market.users.models import UserAddress
from online_market.products.models import Product


class Order(models.Model):
    STATUS_ACCEPTED = 'accepted'
    STATUS_DONE = 'done'
    STATUS_CANCELLED = 'cancelled'
    STATUSES = (
        (STATUS_ACCEPTED, 'Взят в работу'),
        (STATUS_DONE, 'Выполнен'),
        (STATUS_CANCELLED, 'Отменен'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='orders',
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField(
        Product, related_name='orders', through='OrderProduct'
    )
    address = models.ForeignKey(
        UserAddress, on_delete=models.SET_NULL,
        related_name='order', null=True
    )
    total_price = models.IntegerField(verbose_name='Сумма заказа', default=0)
    status = models.CharField(
        max_length=20, choices=STATUSES, default=STATUS_ACCEPTED,
        verbose_name='Статус заказа'
    )
    date_created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    @property
    def prettified_status(self):
        return dict(self.STATUSES)[self.status]

    def __str__(self):
        return ' '.join((str(self.user), str(self.products)))


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
