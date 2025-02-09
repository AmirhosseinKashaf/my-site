from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
# Create your views here.
def home_view (request):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)    

def single_view (request,pid):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status=1)
    post = get_object_or_404(posts,pk=pid)
    all_posts = Post.objects.filter(published_date__lte=timezone.now(),status=1).order_by('published_date')
    current_index = list(all_posts).index(post)
    previous_post = all_posts[current_index - 1] if current_index > 0 else None
    next_post = all_posts[current_index + 1] if current_index < len(all_posts) - 1 else None
    post.counted_views += 1  
    post.save()
    context = {
        'post':post,
        'previous_post': previous_post,
        'next_post':next_post,
        }
    return render(request,'blog/blog-single.html',context) 

def blog_category (request,cat_name):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context) 

# def test (request):
#     Posts = Post.objects.all()
#     context = {'posts':Posts}
#     return render(request,'test.html',context) 
