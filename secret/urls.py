from django.urls import path
from secret import views

app_name = 'secret'

urlpatterns = [
    path('bonus/', views.Bonus.as_view(), name='bonus'),
]