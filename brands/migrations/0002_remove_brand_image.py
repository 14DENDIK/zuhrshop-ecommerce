# Generated by Django 3.0 on 2019-12-12 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='image',
        ),
    ]
