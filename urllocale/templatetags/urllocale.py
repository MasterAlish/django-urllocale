# coding=utf-8
from django import template
from django.conf import settings
from django.template.defaulttags import url, URLNode
from django.utils import translation

register = template.Library()


class I18NURLNode(URLNode):
    def __init__(self, url_node):
        super(I18NURLNode, self).__init__(url_node.view_name, url_node.args, url_node.kwargs, url_node.asvar)

    def render(self, context):
        result = super(I18NURLNode, self).render(context)
        lang = translation.get_language()
        if lang == settings.LANGUAGE_CODE:
            return result
        return "/"+lang+result


@register.tag
def locale_url(parser, token):
    lr = url(parser, token)
    return I18NURLNode(lr)
