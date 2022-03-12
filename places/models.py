from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Интересное место"
        verbose_name_plural = "Интересные места"


class Image(models.Model):

    place = models.ForeignKey(
        Place,
        verbose_name="Место",
        on_delete=models.CASCADE,
        related_name="images"
    )

    order = models.PositiveIntegerField(
        'Порядок картинки',
        default=0,
    )

    image = models.ImageField(
        "Изображение",
        null=True,
        blank=True,
    )

    class Meta(object):
        ordering = ['order']
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"{self.order} {self.place.title}"
