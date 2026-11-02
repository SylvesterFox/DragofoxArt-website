from django import template

from ..models import SocialLink

register = template.Library()


@register.simple_tag
def social_links():
    """Активные ссылки на соцсети в порядке, заданном в админке."""
    return SocialLink.objects.filter(is_active=True)