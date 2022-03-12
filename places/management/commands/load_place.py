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
        new_place_json = new_place_response.json()

        place, created = Place.objects.get_or_create(
            title=new_place_json['title'],
            defaults = {
                'description_short': new_place_json['description_short'],
                'description_long': new_place_json['description_long'],
                'lat': new_place_json['coordinates']['lat'],
                'lon': new_place_json['coordinates']['lng'],
            }
        )

        for image_url in new_place_json['imgs']:

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
