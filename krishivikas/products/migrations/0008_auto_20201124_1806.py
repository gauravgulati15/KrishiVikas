# Generated by Django 3.1.3 on 2020-11-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201124_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
