from django.db import models


class Category(models.Model):
    title = models.CharField("Название", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Color(models.Model):
    name = models.CharField("Цвет", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


class Size(models.Model):
    title = models.CharField("Размер", max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"


class Product(models.Model):
    name = models.CharField("Название товара", max_length=100)
    description = models.CharField("Описание", max_length=150, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', null=True)
    image_1 = models.ImageField("Изображение_1", upload_to="images/")
    image_2 = models.ImageField("Изображение_2", upload_to="images/", null=True)
    image_3 = models.ImageField("Изображение_3", upload_to="images/", null=True)
    image_4 = models.ImageField("Изображение_4", upload_to="images/", null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


# Create your models here.
