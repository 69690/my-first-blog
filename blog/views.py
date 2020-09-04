from django.shortcuts import render
from django.utils import timezone
from .models import Post 

from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

# def story1(request):
#     return render(request, 'blog/stories/story1.html', {})

# def story2(request):
#     return render(request, 'blog/stories/story2.html', {})

# def story3(request):
#     return render(request, 'blog/stories/story3.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html', {})