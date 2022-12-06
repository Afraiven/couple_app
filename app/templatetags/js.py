from django.utils.safestring import mark_safe
from django.template import Library

from datetime import datetime, date
import json


register = Library()


@register.filter(is_safe=True)
def js(obj):
    from app.models import Tekst, Daily
    opened_today = Tekst.objects.filter(seen = 1, opened_date = date.today())
    print("sdasd")
    # return mark_safe(json.dumps(obj))
    return opened_today