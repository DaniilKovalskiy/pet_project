from django.db import models
from django.utils.text import slugify


class ProductCategory(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название категории')
    description = models.TextField(
        verbose_name='Описание', null=True, blank=True)
    slug = models.SlugField(max_length=256, unique=True,
                            db_index=True, verbose_name='URL', null=True, blank=True)

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    short_description = models.TextField(
        verbose_name='Краткое описание', default='Краткое описание')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Категория')
    image = models.ImageField(
        upload_to='products_images', default="vendor/img/users/default_avatar.jpg", null=True, blank=True)
    slug = models.SlugField(max_length=256, unique=True,
                            db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
