from django.urls import path

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('list/', PostListView.as_view(), name='list'),
    path('<int:post_id>/', PostDetailView.as_view(), name='detail'),
    path('<int:post_id>/update/', PostUpdateView.as_view(), name='update'),
    path('<int:post_id>/download', download_pdf, name='download_pdf')
]