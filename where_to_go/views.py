import json

from django.shortcuts import render
from django.urls import reverse

from places.models import Place, Image


def index(request):
    places_points = []
    places = Place.objects.all()

    for place in places:
        about_place = reverse('about-place', args=(place.id, ))

        places_points.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lon, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.pk,
                    "detailsUrl": about_place,
                }
            }
        )

    features = {
        "type": "FeatureCollection",
        "features": places_points
    }

    return render(request, 'index.html', context=features)
