# Generated by Django 4.0.3 on 2022-04-05 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_alter_orders_expected_delivery_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='delivery_address',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 10, 21, 22, 10, 523649), null=True),
        ),
    ]
