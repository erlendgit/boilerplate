from django.conf import settings
from django.http import HttpRequest
from django.utils.translation import get_language


def i18n(request: HttpRequest):
    return {
        'LANGUAGE_CODE': get_language()
    }


def site_info(request: HttpRequest):
    return {
        'SITE_NAME': settings.site_name
    }
