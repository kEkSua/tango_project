from django import template
from rango.models import Category

register = template.Library()


@register.inclusion_tag('rango/categories.html')
def get_category_list(act_category=None):
    return {'categories': Category.objects.all(),
            'act_category': act_category}
