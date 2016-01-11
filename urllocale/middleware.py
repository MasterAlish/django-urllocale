from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from django.utils import translation


class UrlLocaleMiddleware(object):

    def __init__(self):
        if not settings.USE_I18N:
            raise MiddlewareNotUsed()

    def process_request(self, request):
        lang_is_specified_in_url = False
        for lang_code, lang_name in settings.LANGUAGES:
            url_prefix = request.path_info[0:len(lang_code)+2]
            if url_prefix == '/%s/' % lang_code:
                lang_is_specified_in_url = True
                translation.activate(lang_code)
                request.path = request.path[len(lang_code)+1:]
                request.path_info = request.path_info[len(lang_code)+1:]
                request.session['lang_code'] = lang_code
        if not lang_is_specified_in_url:
            translation.activate(settings.LANGUAGE_CODE)
            request.session['lang_code'] = settings.LANGUAGE_CODE

    def process_response(self, request, response):
        if 'Content-Language' not in response:
            response['Content-Language'] = translation.get_language()
        return response
