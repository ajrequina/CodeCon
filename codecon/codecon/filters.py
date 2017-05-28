from django import template
from markdown import markdown
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="markdown")
def markdown_processor(text):
    return mark_safe(markdown(text))
