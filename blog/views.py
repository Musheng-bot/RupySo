from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.views.generic import ListView
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.utils.text import slugify

from blog.forms import PostForm
from blog.models import Post

import md2pdf
import markdown
from weasyprint import HTML

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
    
    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Post.objects.all()
        else:
            queryset = Post.objects.filter(published=True).all()
        return queryset

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    pk_url_kwarg = 'post_id'
    
from playwright.sync_api import sync_playwright

def download_pdf(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    html_content = render_to_string('blog/transform_pdf.html', {'post': post})

    with sync_playwright() as p:
        # 建议开启 chromium，它是兼容性最好的
        browser = p.chromium.launch()
        page = browser.new_page()

        # 1. 设置内容，并等待网络活动停止
        page.set_content(html_content, wait_until="networkidle")

        # 2. 【最关键】等待 MathJax 渲染完成
        # 如果页面有公式，MathJax 3.x 会生成 <mjx-container> 标签
        try:
            # 增加超时时间到 10 秒，确保复杂公式有足够时间加载
            page.wait_for_selector("mjx-container", timeout=10000)
            
            # 3. 额外等待 500ms，防止公式虽然出现了但 CSS 还没排版好（避免错位）
            page.wait_for_timeout(500) 
        except Exception as e:
            # 如果 10 秒都没出公式，可能是这篇文章确实没有公式
            print(f"MathJax timeout or no formulas found: {e}")

        # 4. 生成 PDF，务必开启 print_background
        pdf_bytes = page.pdf(
            format="A4",
            print_background=True,
            margin={"top": "1cm", "bottom": "1cm", "left": "1cm", "right": "1cm"}
        )
        browser.close()

    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{post.title}.pdf"'
    return response