from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView

from project.forms import ProjectForm
from project.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'project/list.html'
    context_object_name = 'project_list'
    paginate_by = 10

    def get_queryset(self):
        return Project.objects.all().order_by('-start_date')

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/detail.html'
    context_object_name = 'project'

    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class ProjectCreateView(UserPassesTestMixin, FormView):
    template_name = 'project/create.html'
    form_class = ProjectForm

    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            # commit=False 表示先不保存到数据库，先拿出一个实例
            project = form.save(commit=False)

            # 读取上传的文件内容
            uploaded_file = request.FILES.get('content_file')
            if uploaded_file:
                # 读取字节流并解码为字符串
                file_content = uploaded_file.read().decode('utf-8')
                project.description = file_content  # 赋值给 description 字段

            project.save()
            return redirect('project:index')
        else:
            return render(request, 'project/create.html', {'form': form})