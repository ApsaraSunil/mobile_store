# Generated by Django 4.0.3 on 2022-04-12 15:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0003_mobiles_image'),
        ('customer', '0012_alter_feedback_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='owner.mobiles'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 17, 21, 23, 37, 325655), null=True),
        ),
    ]
