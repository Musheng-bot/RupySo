from django import forms
from project.models import Project

class ProjectForm(forms.ModelForm):
    content_file = forms.FileField(
        label="描述文件 (.md)",
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.md,.txt'})
    )

    class Meta:
        model = Project
        exclude = ['description']
        widgets = {
            # 移除所有的 placeholder 属性
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'source_code_url': forms.URLInput(attrs={'class': 'form-control'}),
            'project_url': forms.URLInput(attrs={'class': 'form-control'}),
            'is_finished': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }