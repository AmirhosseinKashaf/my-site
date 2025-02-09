from django import template
from blog.models import Post,Category
from django.utils import timezone


register = template.Library()

@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts(args=3):
   posts = Post.objects.filter(published_date__lte=timezone.now(),status=1)[:args]
   return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories(args=3):
   posts = Post.objects.filter(published_date__lte=timezone.now(),status=1)
   categories = Category.objects.all()
   cat_dict = {}
   for name in categories:
      cat_dict[name] = posts.filter(category=name).count()
   return {'categories':cat_dict}