from django.db import models

# Create your models here.
from django.utils.html import format_html


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")

    def __str__(self):
        return f"{self.title}"


class Image(models.Model):

    place = models.ForeignKey(
        Place,
        verbose_name="Место",
        on_delete=models.CASCADE,
        related_name="images"
    )

    order = models.PositiveIntegerField(
        'Порядок картинки',
        blank=False,
        null=False
    )

    image = models.ImageField(
        "Изображение",
        null=True,
        blank=True
    )

    class Meta(object):
        ordering = ['order']

    def __str__(self):
        return f"{self.order} {self.image}"
