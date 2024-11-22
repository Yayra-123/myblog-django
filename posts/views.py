from django.shortcuts import render ,redirect
from posts.models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

@login_required
def index(request):
    posts=Post.objects.order_by('-id').all()
    paginator=Paginator(posts,6)
    page_number=request.GET.get('page')
    page_object=paginator.get_page(page_number)
    post_number=posts.count()
    message=f'{post_number} posts:'
    if post_number==1:
        message=f'{post_number}post:'
        
    context={
        'posts':page_object,
        'post_number':post_number,
        'message':message,
    }
    
    return render(request,'posts/index.html',context)

@login_required
def show(request,id):
    post=Post.objects.get(id=id)
    context ={
        'post':post,
    }
    return render(request,'posts/show.html', context )

@login_required
def new_post(request):
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            return redirect('posts:index')
    else:
        form=PostForm()
        context={
		 'form':form,
		}
    return render(request,'posts/new_post.html',context)
 
@login_required
def update_post(request, id):
    post=Post.objects.get(id=id)
    
    if post.user == request.user:
        if request.method == 'POST':	
            form=PostForm(request.POST,request.FILES,instance=post)
            if form.is_valid():
                form.save()
            return redirect('posts:index')
        else:
            form=PostForm(instance=post)
    else:
        raise Http404
    context={
        'form':form,
        'post':post,
        }
    return render(request,'posts/update_post.html', context)
    

@login_required
def delete_post(request,id):
    post=Post.objects.get(id=id)
    if post.user == request.user:
        
        post.delete()
    else:
        raise Http404
    return redirect('posts:index')
    return render(request,'posts/delete.html')

@login_required
def search_posts(request):
    
    search=request.GET.get('search')
    posts=Post.objects.filter(Q(title__icontains=search) |
                              Q(content__icontains=search) |
                              Q(image__icontains=search))
    
    # posts=Post.objects.order_by('-id').all()
    post_number=posts.count()
    message=f'{post_number} results:'
    if post_number==1:
        message=f'{post_number}result:'
    context={
        'posts':posts,
        'message':message,
    }
    return render(request,'posts/search_posts.html',context)