# Generated by Django 3.1 on 2020-09-20 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_order_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
    ]