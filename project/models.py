from django.db import models
from django.urls.base import reverse_lazy

class Project(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='项目名')
    short_description = models.CharField(max_length=100, verbose_name='项目简述')
    description = models.TextField(verbose_name='项目详述') # 存md文本
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug')

    start_date = models.DateField(verbose_name='开始时间')
    end_date = models.DateField(null=True, blank=True, verbose_name='结束时间')
    source_code_url = models.URLField(null=True, blank=True, verbose_name='源码链接')
    project_url = models.URLField(null=True, blank=True, verbose_name='项目展示链接')

    is_finished = models.BooleanField(default=False, verbose_name='是否已完结')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("project:detail", kwargs={"slug": self.slug})
