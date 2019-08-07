from django import template
register = template.Library()

@register.filter()
def can_edit(user, obj):
    if user.has_perm(obj):
        return True
    else:
        return False
    