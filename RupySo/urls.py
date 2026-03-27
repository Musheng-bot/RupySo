from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls.static import static


def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', include('about.urls', namespace='about')),
    path('project/', include('project.urls', namespace='project')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('secret/', include('secret.urls', namespace='secret')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
