# Generated by Django 2.2.3 on 2024-05-28 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promo_code', '0001_initial'),
        ('orders', '0003_order_shipping_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='promo_code',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promo_code.PromoCode'),
        ),
    ]
