from django.shortcuts import render, redirect,get_object_or_404
from .forms import PostForm
from .models import Post
# Create your views here.

def home(request):
    post = Post.objects
    return render(request,'lend/home.html',{'post': post})

def content(request,post_id):
    blog_detail = get_object_or_404(Post,pk=post_id)
    return render(request,"lend/content.html",{"content":blog_detail})
def lend(request):
    return render(request, 'lend/lend.html')

def new(request):
    return render(request, 'lend/new.html')

def postcreate(request):
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # return redirect('/')
            return render(request,'lend/home.html',{"a": post})
    else :
        form = PostForm()
        return render(request, 'lend/new.html', {'form': form})
