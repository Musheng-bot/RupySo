from django.contrib.auth.mixins import UserPassesTestMixin
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.views.generic import ListView

from blog.forms import PostForm, PostImageFormSet
from blog.models import Post


class PostCreateView(UserPassesTestMixin, CreateView):  # 沿用你之前的权限 Mixin
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
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

        # 1. 同时校验主表和从表 (不合法的直接返回并报错)
        if form.is_valid() and images.is_valid():
            # 2. 只有都通过了，才开事务干活
            with transaction.atomic():
                # 保存主表
                self.object = form.save()
                # 绑定主外键并保存从表
                images.instance = self.object
                images.save()

            # 3. 注意：这里直接跳转成功页面，不再调用 super().form_valid
            # 因为 super 还会去 save 那个已经 save 过的 form
            return redirect(self.get_success_url())
        else:
            # 4. 如果不合法，返回 form_invalid 渲染错误信息
            return self.form_invalid(form)

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


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    pk_url_kwarg = 'post_id'
    template_name = 'blog/post_form.html'  # 复用创建页面的模板
    context_object_name = 'post'

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'post_id': self.object.pk})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            # 传入 instance=self.object 是编辑模式的关键
            data['images'] = PostImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['images'] = PostImageFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        images = context['images']

        # 1. 先校验 FormSet
        if images.is_valid():
            with transaction.atomic():
                # 2. 调用 super().form_valid(form)
                # 这行会自动执行 self.object = form.save() 并返回一个 HttpResponseRedirect
                response = super().form_valid(form)

                # 3. 此时主表 self.object 已经存好了，处理图片
                images.instance = self.object
                images.save()

                return response  # 返回父类生成的 redirect
        else:
            # 如果图片不合法，直接走失败流程
            return self.form_invalid(form)


    def test_func(self):
        return self.request.user.is_staff


