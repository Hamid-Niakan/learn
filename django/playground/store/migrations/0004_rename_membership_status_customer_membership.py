# Generated by Django 4.2.5 on 2023-09-07 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_price_product_unit_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='membership_status',
            new_name='membership',
        ),
    ]
