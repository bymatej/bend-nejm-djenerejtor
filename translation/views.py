from django.http import HttpRequest, HttpResponse


def translate(request: HttpRequest):
    return HttpResponse("translate")
