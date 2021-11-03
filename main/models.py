from django.db import models


class Review(models.Model):
    name = models.CharField("ФИО клиента", max_length=100)
    country = models.CharField("Город проживание", max_length=100)
    image = models.ImageField("Изображение", upload_to="images/",)
    text = models.TextField("Отзыв")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Slaider(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    sub_title = models.CharField("Подзаголовок", max_length=50)
    image = models.ImageField("Изображение", upload_to="images/",)
    button_name = models.CharField("Название кнопки", max_length=20)
    button_url = models.URLField("URL для кнопки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость в слайдере"
        verbose_name_plural = "Новости в слайдере"


# Create your models here.
