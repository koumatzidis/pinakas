# scovie/templatetags/dict_extras.py
from django import template

register = template.Library()

@register.filter
def get_item(value, key):
    try:
        return value.get(key)
    except AttributeError:
        return value  # Just return the value if it's not a dict

@register.filter
def get_item(dictionary, key):
    if isinstance(dictionary, dict):
        return dictionary.get(key, "")
    return ""

