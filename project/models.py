from django.db import models
from django.urls.base import reverse_lazy

class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short_description = models.CharField(max_length=100, default="")
    description = models.TextField() # 存md文本
    slug = models.SlugField(max_length=100, unique=True, default="")

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    source_code_url = models.URLField(null=True, blank=True)
    project_url = models.URLField(null=True, blank=True)

    is_finished = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("project:detail", kwargs={"slug": self.slug})
