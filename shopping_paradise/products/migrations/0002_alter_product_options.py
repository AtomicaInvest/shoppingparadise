# Generated by Django 3.2.9 on 2021-11-14 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': (('can_put_on_sale', 'Put product on sale'),)},
        ),
    ]
