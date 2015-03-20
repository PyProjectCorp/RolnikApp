from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Homepage


class HomepageView(ListView):
    model = Homepage
    template_name = 'home.html'