from django import template
from django.template.defaultfilters import stringfilter

from core.constants import MESSAGE_ICONS


register = template.Library()


@register.filter
@stringfilter
def icon(value):
    return MESSAGE_ICONS.get(value, "fa-file")
