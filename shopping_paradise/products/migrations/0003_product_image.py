# Generated by Django 3.2.9 on 2021-11-28 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='products/'),
            preserve_default=False,
        ),
    ]
