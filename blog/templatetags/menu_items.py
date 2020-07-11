from django import template
from blog.models import Skill
from users.models import Profile
from django.contrib.auth.models import User
from django.db import models

register = template.Library()

@register.inclusion_tag('blog/menu_items.html')
def menu_items():
    user = User.objects.first()
    context = {
        'items': Skill.objects.filter(author=user) #filter(author=request.user)
    }
    return context #need to check user