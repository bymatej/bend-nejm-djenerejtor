import requests
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

url = 'https://translate.googleapis.com/translate_a/single'
params = {
    'client': 'gtx',
    'dt': 't',
}


@csrf_exempt
def translate(request: HttpRequest):
    # Obtain English name
    english_band_name = str(request.POST['english_band_name'])

    # Translate
    translated = __purposefully_mess_up_the_band_name(english_band_name)

    # Return
    return HttpResponse(translated)


def __purposefully_mess_up_the_band_name(english_band_name: str) -> str:
    german = __translate_en_de(english_band_name)
    french = __translate_de_fr(german)
    croatian = __translate_fr_hr(french)
    return croatian


def __translate_en_de(string: str) -> str:
    params.update({'q': string,
                   'sl': 'en',
                   'tl': 'de'})
    return __translate(params)


def __translate_de_fr(string: str) -> str:
    params.update({'q': string,
                   'sl': 'de',
                   'tl': 'fr'})
    return __translate(params)


def __translate_fr_hr(string: str) -> str:
    params.update({'q': string,
                   'sl': 'fr',
                   'tl': 'hr'})
    return __translate(params)


def __translate(parameters) -> str:
    response = requests.get(url=url, params=parameters)
    return response.json()[0][0][0]
