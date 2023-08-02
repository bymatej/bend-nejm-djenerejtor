import random

from django.http import HttpRequest, HttpResponse

from .models import Bands


def get_random_name(request: HttpRequest):
    all_bands = Bands.objects.all()
    all_names = [band.name for band in all_bands]
    return HttpResponse(random.choice(all_names))
