from django.shortcuts import render
from django.views.generic import ListView, DetailView,  FormView
from .models import Animals
from animals.forms import AnimalsForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class AnimalsAddView(FormView):
    form_class = AnimalsForm
    template_name = 'animals/animals_dodaj.html'
    success_url= '/animals'
    def form_valid(self, form):
        form.save()
        return super(AnimalsAddView, self).form_valid(form)


class AnimalsView(ListView):
    model = Animals
    template_name = 'animals/animals_list.html'
