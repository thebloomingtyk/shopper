# Generated by Django 4.1.3 on 2022-12-05 12:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_order_city_remove_order_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='phone_number'),
        ),
    ]