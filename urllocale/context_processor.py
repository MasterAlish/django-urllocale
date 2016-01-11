from django.conf import settings


def urllocale(request):
    lang_code = settings.LANGUAGE_CODE
    if 'lang_code' in request.session:
        lang_code = request.session['lang_code']
    return {'lang_code': lang_code}
