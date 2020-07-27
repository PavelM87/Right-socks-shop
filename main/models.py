from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator


class Product(models.Model):
    slug = models.SlugField(unique=True, null=True, blank=True)
    title = models.CharField('Название', max_length=50)
    short_descr = models.CharField('Краткое описание', max_length=100)
    full_descr = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='images/')
    specific = models.TextField('Характеристики')
    price = models.IntegerField('Цена')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    size = models.CharField('Размеры', max_length=100)
    color = models.CharField('Цвет', max_length=50)
    material = models.CharField('Материал', max_length=150)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристики товаров'

"""class Mail(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True)
    phone = models.CharField('Номер телефона', max_length=30, blank=True)
    email = models.EmailField('Почта')
    topic = models.CharField('Тема', max_length=100, blank=True)
    message = models.TextField('Сообщение')"""

def slug_generator(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender = Product)




