from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
