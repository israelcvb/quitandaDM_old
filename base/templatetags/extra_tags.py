from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag
def current_time():
    return datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
