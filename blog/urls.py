from django.urls import path

from blog.views import PostCreateView, PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('list/', PostListView.as_view(), name='list'),
    path('<int:post_id>/', PostDetailView.as_view(), name='detail'),
]