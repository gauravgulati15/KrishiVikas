# Generated by Django 3.1.3 on 2020-11-24 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20201124_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.customer'),
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]
