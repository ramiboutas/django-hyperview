from django import template
from django.utils.safestring import mark_safe
from django.middleware.csrf import get_token

register = template.Library()


@register.simple_tag
def hv_csrf_token(request):
    token = get_token(request) or "NOTPROVIDED"
    content = f'<text-field hide="true" name="csrfmiddlewaretoken" value="{token}" />'
    return mark_safe(content)
