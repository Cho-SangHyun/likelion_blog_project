from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'home.html')

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    blogs = Blog.objects.all() 
    return render(request, 'detail.html', {'details' : details, 'blogs' : blogs}) # details

def intro(request):
    return render(request, 'intro.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs' : blogs})

def new(request):
    blogs = Blog.objects.all()
    return render(request, "new.html", {'blogs' : blogs})

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.writer = request.GET['writer']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()

    return redirect('/blog/' + str(blog.id))

def edit(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blogs = Blog.objects.all() 
    return render(request, 'edit.html', {'blogs' : blogs, 'blog' : blog})

def update(request, blog_id):
    update_blog = Blog.objects.get(id=blog_id)
    update_blog.title = request.GET['title']
    update_blog.writer = request.GET['writer']
    update_blog.body = request.GET['body']
    update_blog.pub_date = timezone.datetime.now()

    update_blog.save()
    return redirect("detail",update_blog.id)

def delete(request, blog_id):
    delete_blog = Blog.objects.get(id=blog_id)
    delete_blog.delete()
    return redirect("blog")
