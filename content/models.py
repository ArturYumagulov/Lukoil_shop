from django.db import models


class Slider(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)
    name = models.CharField(max_length=30, verbose_name="Название слайдера")
    image = models.ImageField(upload_to='slider_image/')
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    sub_title = models.CharField(max_length=50, verbose_name="Подзаголовок")
    button = models.CharField(max_length=30, verbose_name="Текст кнопки")
    button_url = models.CharField(max_length=255, verbose_name="Путь кнопки", blank=True, null=True)
    button_active = models.BooleanField(verbose_name="Вывести кнопку", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдер"
        ordering = ['created_date']

