# Generated by Django 4.0.2 on 2022-03-11 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_image_options_remove_image_image_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.PositiveIntegerField(verbose_name='Порядок картинки'),
        ),
    ]
