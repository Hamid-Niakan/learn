# Generated by Django 5.0 on 2024-01-13 21:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_cartitem_cart_alter_cartitem_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.cart'),
        ),
    ]
