from django.contrib import admin
from .models import Post, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 3  # 默认显示3个空槽
    max_num = 9 # 强制限制最大上传数为9张

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]
    list_display = ('title', 'created_at')