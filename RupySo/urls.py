from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


def index(request):
    return render(request, 'index.html')

def about(request):
    tech_stack = [
        {"name": "Django-Web开发", "percentage": 85},
        {"name": "AI-人工智能", "percentage": 5},
        {"name": "Robotics", "percentage": 10},
    ]
    return render(request, 'about.html', context=locals())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('project/', include('project.urls', namespace='project')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('secret/', include('secret.urls', namespace='secret')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
