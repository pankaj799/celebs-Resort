from django import template

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})

#
# @register.filter(name='add_placeholder')
# def add_placeholder(field, placeholder):
#     return field.as_widget(attrs={"title": placeholder})
