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
    post.counted_views += 1  
    post.save()
    context = {'post':post}
    return render(request,'blog/blog-single.html',context) 

# def test (request):
#     Posts = Post.objects.all()
#     context = {'posts':Posts}
#     return render(request,'test.html',context) 
