import requests
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse


def generate(request: HttpRequest):
    # Get random name
    random_name = __get_random_band_name(request)

    # Translate name
    translated_name = __translate_band_name(request, random_name)

    # Return translated value
    return render(request=request, template_name='generator/index.html', context={'generated_name': translated_name})


def __get_random_band_name(request: HttpRequest) -> str:
    get_random_band_name_url = reverse('get_random_name')  # Generate the URL based on the URL pattern name
    response = requests.get(request.build_absolute_uri(get_random_band_name_url))
    return response.text


def __translate_band_name(request: HttpRequest, band_name: str) -> str:
    # Translate randomly generated band name to Croatian
    translate_to_croatian_url = reverse('translate')  # Generate the URL based on the URL pattern name
    response = requests.post(
        request.build_absolute_uri(translate_to_croatian_url),
        data={'english_band_name': band_name}
    )  # Translate randomly picked name from __get_random_band_name to Croatian
    return response.text
