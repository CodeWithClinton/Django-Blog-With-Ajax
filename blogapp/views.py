from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'blog_index.html', {'posts': posts})

def blog_detail(request, slug):
    post = Post.objects.get(slug = slug)
    comments = post.comments.all()
    new_comment = None
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return JsonResponse({'commenter': new_comment.author, 'msg': new_comment.body})
    return render(request, 'blog_detail.html', {'post': post, 'comments':comments,'form':form, 'new_comment': new_comment})
