from django.db import models

class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    short_descr = models.CharField('Краткое описание', max_length=100)
    full_descr = models.TextField('Описание')
    image = models.ImageField('Изображение')
    specific = models.TextField('Характеристики')
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Specification(models.Model):
    title = models.CharField('Название', max_length=50)
    size = models.CharField('Размеры', max_length=100)
    color = models.CharField('Цвет', max_length=50)
    material = models.CharField('Материал', max_length=50)
    print = models.BinaryField('Рисунок', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

"""class Mail(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True)
    phone = models.CharField('Номер телефона', max_length=30, blank=True)
    email = models.EmailField('Почта')
    topic = models.CharField('Тема', max_length=100, blank=True)
    message = models.TextField('Сообщение')"""







