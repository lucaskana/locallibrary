# Generated by Django 3.2.7 on 2021-10-06 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='info',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
