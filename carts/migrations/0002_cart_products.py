# Generated by Django 2.2.3 on 2024-05-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilito', '0004_product_image'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='carts.CartProducts', to='facilito.Product'),
        ),
    ]
