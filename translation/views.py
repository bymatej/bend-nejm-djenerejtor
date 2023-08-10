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
    swahili = __translate_en_sw(english_band_name)
    german = __translate_sw_de(swahili)
    french = __translate_de_fr(german)
    kurdish = __translate_fr_ckb(french)
    croatian = __translate_ckb_hr(kurdish)
    croatian = __translate_auto_hr(croatian)
    return croatian


def __translate_en_sw(string: str) -> str:
    params.update({'q': string,
                   'sl': 'en',
                   'tl': 'sw'})
    return __translate(params)


def __translate_sw_de(string: str) -> str:
    params.update({'q': string,
                   'sl': 'sw',
                   'tl': 'de'})
    return __translate(params)


def __translate_de_fr(string: str) -> str:
    params.update({'q': string,
                   'sl': 'de',
                   'tl': 'fr'})
    return __translate(params)


def __translate_fr_ckb(string: str) -> str:
    params.update({'q': string,
                   'sl': 'fr',
                   'tl': 'ckb'})
    return __translate(params)


def __translate_ckb_hr(string: str) -> str:
    params.update({'q': string,
                   'sl': 'ckb',
                   'tl': 'hr'})
    return __translate(params)


def __translate_auto_hr(string: str) -> str:
    params.update({'q': string,
                   'sl': 'auto',
                   'tl': 'hr'})
    return __translate(params)


def __translate(parameters) -> str:
    response = requests.get(url=url, params=parameters)
    return response.json()[0][0][0]
