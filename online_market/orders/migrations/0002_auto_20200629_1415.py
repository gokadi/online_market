# Generated by Django 2.2 on 2020-06-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', through='orders.OrderProduct', to='products.Product'),
        ),
    ]
