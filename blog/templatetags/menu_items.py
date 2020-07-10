from django import template
from blog.models import Skill


register = template.Library()

@register.inclusion_tag('blog/menu_items.html', takes_context=True)
def menu_items(context):
    return {'items': Skill.objects.all()} #need to check user