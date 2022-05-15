from django.conf import settings

from core.constants import MESSAGE_ICONS


def page_title(request):
    return {"page_title": settings.PAGE_TITLE}


def msg_icon(request):
    return {"message_icon": MESSAGE_ICONS}
