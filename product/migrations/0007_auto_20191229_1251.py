# Generated by Django 3.0 on 2019-12-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='condition',
            field=models.CharField(choices=[('new', 'NEW'), ('used', 'USED')], default='new', max_length=4),
        ),
    ]
