# Generated by Django 4.2.2 on 2023-07-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='vendor/img/users/default_avatar.jpg', null=True, upload_to='products_images'),
        ),
    ]
