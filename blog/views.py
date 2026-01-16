from django.contrib.auth.mixins import UserPassesTestMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic import ListView

from blog.forms import PostForm, PostImageFormSet
from blog.models import Post


class PostCreateView(UserPassesTestMixin, CreateView):  # 沿用你之前的权限 Mixin
    model = Post
    form_class = PostForm
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:list')

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['images'] = PostImageFormSet(self.request.POST, self.request.FILES)
        else:
            data['images'] = PostImageFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        images = context['images']

        # 使用事务，确保 Post 和图片要么同时成功，要么同时失败
        with transaction.atomic():
            self.object = form.save()
            if images.is_valid():
                images.instance = self.object
                images.save()
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    # 关键优化：预加载关联的图片数据
    queryset = Post.objects.prefetch_related('images').all()

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    pk_url_kwarg = 'post_id'
