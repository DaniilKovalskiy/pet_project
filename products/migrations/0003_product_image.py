# Generated by Django 3.2.13 on 2023-07-15 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productcategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='static/vendor/img/products/no_photo.png', upload_to='products_images'),
        ),
    ]