import requests
from urllib.parse import urlparse

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Load new place information'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str)

    def handle(self, *args, **options):
        json_url = options['json_url']
        new_place_response = requests.get(json_url)
        new_place_response.raise_for_status()
        place_raw = new_place_response.json()

        place, created = Place.objects.get_or_create(
            title=place_raw['title'],
            defaults = {
                'description_short': place_raw['description_short'],
                'description_long': place_raw['description_long'],
                'lat': place_raw['coordinates']['lat'],
                'lon': place_raw['coordinates']['lng'],
            }
        )

        for image_url in place_raw['imgs']:

            place_image = Image.objects.create(place=place)
            name = urlparse(image_url).path.split('/')[-1]

            image_response = requests.get(image_url)
            image_response.raise_for_status()
            image_content = ContentFile(image_response.content)

            place_image.image.save(
                name,
                image_content,
                save=True
            )
