from django import template
from blog.models import Skill
from users.models import Profile
from django.contrib.auth.models import User
from django.db import models

register = template.Library()

@register.inclusion_tag('blog/menu_items.html')
def menu_items():
    return {'items': Skill.objects.all()} #need to check user