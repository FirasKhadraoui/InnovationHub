# Generated by Django 3.2 on 2022-03-01 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]