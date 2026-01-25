from django.shortcuts import render
from django.views.generic import TemplateView


class Bonus(TemplateView):
    template_name = 'bonus.html'
