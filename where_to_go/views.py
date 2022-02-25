import json

from django.shortcuts import render
from places.models import Place, Image

from pprint import  pprint


def index(request):
    places_points = []
    places = Place.objects.all()
    for place in places:

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
                    "detailsUrl": "../static/places/moscow_legends.json"
                }
            }
        )

    features = {
        "type": "FeatureCollection",
        "features": places_points
    }

    return render(request, 'index.html', context=features)
