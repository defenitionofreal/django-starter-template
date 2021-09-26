from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag('templatetags/custom_tag.html', takes_context=True)
def custom_tag(context, value):
    pass