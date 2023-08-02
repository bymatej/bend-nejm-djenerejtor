from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
import requests


def generate(request: HttpRequest):
    # Get random name
    get_random_band_name_url = reverse('get_random_name')  # Generate the URL based on the URL pattern name
    response = requests.get(request.build_absolute_uri(get_random_band_name_url))
    # data = response.json()
    # random_band_names = data['bands']
    # print(random_band_names)

    # Translate

    # Return result
    return HttpResponse(response)
