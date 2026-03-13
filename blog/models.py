from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = CKEditor5Field(config_name='extends', verbose_name='内容')
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '博文'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
