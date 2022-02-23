from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")

    def __str__(self):
        return f"{self.title}"


class Image(models.Model):

    orders = [
        (1, '1'),
        (2, '2'),
    ]

    place = models.ForeignKey(
        Place,
        verbose_name="Место",
        on_delete=models.CASCADE,
        related_name="images"
    )

    image_order = models.PositiveSmallIntegerField(
        'Порядок картинки',
        choices=orders
    )
    image = models.ImageField(
        "Изображение",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.image_order} {self.place}"

