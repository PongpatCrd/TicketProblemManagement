import urllib
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    query.update(kwargs)
    return urllib.parse.urlencode(query)

@register.filter(is_safe=True)
def in_special_member(text):
    special_member_list = [
        'pongpat.cho@majorcineplex.com',
        'nipit.pat@majorcineplex.com',
        'info@nilecon.com'
    ]

    if text.lower() in special_member_list:
        return True
    else:
        return False