# blog/forms.py
from django import forms
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["published"].widget.attrs.update({"class": "form-check-input"})
        
    class Meta:
        model = Post
        fields = ("title", "content", "published")
        widgets = {
            # 这里的 "extends" 必须和你 settings.py 里的 CKEDITOR_5_CONFIGS 键名一致
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }
