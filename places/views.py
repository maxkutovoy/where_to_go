from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from places.models import Place, Image

# Create your views here.
def hi(request):
    return render(request, 'hi')


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