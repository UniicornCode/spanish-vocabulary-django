from django import template

register = template.Library()


@register.simple_tag
def multiple_args_tag(your_object, first_property, second_property):
    first_property = str(first_property)
    return your_object[first_property][second_property]
