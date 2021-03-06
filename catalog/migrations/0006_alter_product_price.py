# Generated by Django 3.2.7 on 2021-10-06 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_pricerow_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.OneToOneField(blank=True, help_text='Select a price row for this product', on_delete=django.db.models.deletion.CASCADE, to='catalog.pricerow'),
        ),
    ]
