import random

from django.http import HttpRequest, HttpResponse

from .models import Bands


def get_random_name(request: HttpRequest):
    all_bands = Bands.objects.all()
    all_names = [band.name for band in all_bands]
    selected_names = random.sample(all_names, 2)
    return HttpResponse(__get_combined_name(selected_names))


def __get_combined_name(names: []) -> str:
    if len(names) != 2:
        raise ValueError("The input array must contain exactly two strings")

    words1 = names[0].split()
    words2 = names[1].split()

    first_word = random.choice([words1[0], words1[-1]])
    second_word = random.choice([words2[0], words2[-1]])

    return f"{first_word} {second_word}"
