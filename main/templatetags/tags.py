from django import template
from main.models import *

register = template.Library()


@register.simple_tag(name='draw_menu')
def draw_menu(name):
    menu = Menu.objects.get(name=name)
    items = MenuItem.objects.filter(menu=menu)

    result = '<ul>'
    for i in items:
        result += f"<li><a href='{i.url}'>{i}</a></li>"
    result += '</ul>'

    return result
