from django import forms
from blog.models import Post, PostImage

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }

# 创建一个内联表单集
PostImageFormSet = forms.inlineformset_factory(
    Post, PostImage,
    fields=('image', 'caption'),
    extra=1,       # 默认显示 1 个上传框
    max_num=9,     # 严格限制最多 9 张
    can_delete=True, # 允许在编辑时删除图片
    widgets={
        'image': forms.FileInput(attrs={'class': 'form-control'}),
        'caption': forms.TextInput(attrs={'class': 'form-control'}),
    }
)