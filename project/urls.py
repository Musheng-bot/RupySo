from django.urls import path
from project.views import ProjectListView, ProjectDetailView

app_name = 'project'

urlpatterns = [
    path('', ProjectListView.as_view(), name='index'),
    path('<slug:slug>', ProjectDetailView.as_view(), name='detail'),
]