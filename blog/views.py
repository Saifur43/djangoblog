from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    queryset = Post.objects.all().order_by('-date')
    template_name = 'blog.html'
    paginate_by = 3


class PostDetailView(DetailView):
    template_name = 'post.html'
    queryset = Post.objects.all()


def contact(request):
    return render(request, 'contact.html')
