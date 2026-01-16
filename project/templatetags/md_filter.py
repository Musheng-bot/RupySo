import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# 在函数外部初始化，只在服务器启动时执行一次
MD_ENGINE = markdown.Markdown(extensions=[
    'extra',
    'codehilite',
    'toc',
])


@register.filter(name='markdown')
def do_markdown(value):
    if not value:
        return ""
    return mark_safe(MD_ENGINE.convert(value))