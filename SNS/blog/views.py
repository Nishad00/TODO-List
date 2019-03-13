from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView,  CreateView, UpdateView,  DeleteView

def home(request):

    context = {
        'posts':Post.objects.all() 
    }
    return render(request,'blog/home.html', context)


class PostListView( ListView ):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 7



class PostCreateView(  CreateView ):
    model = Post
    fields = ['title','content']

    
class PostUpdateView( UpdateView ):
    model = Post
    fields = ['title','content']



class PostDeleteView( DeleteView ):
    model = Post
    success_url = '/'
