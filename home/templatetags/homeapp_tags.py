from django import template
import six
from home.models import HomePage 

register = template.Library()


# @register.simple_tag()
# def post_date_url(post, blog_page):
#     post_date = post.date
#     url = blog_page.url + blog_page.reverse_subpage(
#         'post_by_date_slug',
#         args=(
#             post_date.year,
#             '{0:02}'.format(post_date.month),
#             '{0:02}'.format(post_date.day),
#             post.slug,
#         )
#     )
#     return url

@register.inclusion_tag('_shared/footer.html', takes_context=True)
def show_footer(context):
    home = HomePage.objects.live().first()
    print(home)
    return {'home' : home}

@register.inclusion_tag('_shared/navbar.html', takes_context=True)
def show_navbar(context):
    home = HomePage.objects.live().first()
    menuitems = home.get_children().live().in_menu()
    print(home)
    return {'home' : home, 'menuitems' : menuitems }

