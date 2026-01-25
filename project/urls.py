from django.urls import path
from project.views import ProjectListView, ProjectDetailView, ProjectCreateView

app_name = 'project'

urlpatterns = [
    path('list/', ProjectListView.as_view(), name='index'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('<slug:slug>/', ProjectDetailView.as_view(), name='detail'),
]