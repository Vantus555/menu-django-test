from django import template
from django.urls import reverse
from main.models import *

register = template.Library()
DEFAULT_MARGIN = 10


def getDetails(request, items, item, margin):
    is_active = False
    result = f"<details style='margin-left: {margin}px'>"

    sub_items = items.filter(parent_item = item)

    try:
        url = reverse(item.url)
    except:
        url = item.url

    if url.endswith(request.get_full_path()):
        is_active = True
        result = result.replace("<details", "<details open")
        result += f'<summary class="active"><a href="{url}">{item}</a></summary>'
    else:
        result += f'<summary><a href="{url}">{item}</a></summary>'

    for i in sub_items:
        is_open, sub_res = getDetails(request, items, i, margin + DEFAULT_MARGIN)
        if is_open:
            is_active = is_open
            result = result.replace("<details", "<details open", 1)
        result += sub_res

    result += "</details>"
    
    return is_active, result

@register.simple_tag(name='draw_menu')
def draw_menu(request, name):
    menu = Menu.objects.get(name=name)
    items = MenuItem.objects.filter(menu=menu)

    result = ''
    for i in items:
        if i.parent_item == None:
            is_open, sub_res = getDetails(request, items, i, 0)
            result += sub_res

    return result
