from django.conf import settings


def page_title(request):
    return {"page_title": settings.PAGE_TITLE}
