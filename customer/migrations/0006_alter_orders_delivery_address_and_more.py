# Generated by Django 4.0.3 on 2022-04-04 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_orders_expected_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delivery_address',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 9, 21, 51, 16, 712496), null=True),
        ),
    ]