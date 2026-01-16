from django.views.generic import ListView, DetailView

from project.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'project_list'
    paginate_by = 10

    def get_queryset(self):
        return Project.objects.all().order_by('-start_date')

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'project'

    slug_field = 'slug'
    slug_url_kwarg = 'slug'
