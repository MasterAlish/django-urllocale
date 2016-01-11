from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils import translation


def locale_reverse(viewname, urlconf=None, args=None, kwargs=None, prefix=None, current_app=None):
    result = reverse(viewname, urlconf, args, kwargs, prefix, current_app)
    lang = translation.get_language()
    if lang == settings.LANGUAGE_CODE:
        return result
    return "/"+lang+result