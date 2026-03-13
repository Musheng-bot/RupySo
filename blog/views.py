from django.contrib.auth.mixins import UserPassesTestMixin
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.views.generic import ListView

from blog.forms import PostForm
from blog.models import Post


class PostCreateView(UserPassesTestMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:list')

    def test_func(self):
        return self.request.user.is_staff


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    pk_url_kwarg = "post_id"
    template_name = "blog/post_form.html"
    context_object_name = "post"

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'post_id': self.object.pk})

class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    pk_url_kwarg = 'post_id'

