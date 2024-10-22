from django import template

register = template.Library()

@register.filter
def split_days(value):
    return value.split(',')