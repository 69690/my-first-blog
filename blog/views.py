from django.shortcuts import render
from django.utils import timezone
from .models import Post 

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def story1(request):
    return render(request, 'blog/stories/story1.html', {})

def story2(request):
    return render(request, 'blog/stories/story2.html', {})

def story3(request):
    return render(request, 'blog/stories/story3.html', {})