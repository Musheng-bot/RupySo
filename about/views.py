from django.shortcuts import render
from about.models import Occupation, Reward

def index(request):
    occupations = Occupation.objects.all()
    rewards = Reward.objects.all()
    tech_stack = [
        {"name": "Django-Web开发", "percentage": 85},
        {"name": "AI-人工智能", "percentage": 5},
        {"name": "Robotics", "percentage": 10},
    ]
    return render(request, 'about/index.html', context=locals())
