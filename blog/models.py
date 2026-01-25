from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '博文'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/%Y/%m/', verbose_name='图片')
    caption = models.CharField(max_length=100, blank=True, null=True, verbose_name='图片说明')

    class Meta:
        verbose_name = '博文图片'
        verbose_name_plural = verbose_name
