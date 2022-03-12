import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
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


def about_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    feature_details = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
        }
    }

    return JsonResponse(feature_details, json_dumps_params={'ensure_ascii': False, 'indent': 2})