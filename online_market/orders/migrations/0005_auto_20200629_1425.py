# Generated by Django 2.2 on 2020-06-29 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orderproduct_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='count',
            new_name='amount',
        ),
    ]
