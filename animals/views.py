from django.shortcuts import render
from django.views.generic import ListView, DetailView,  FormView
from .models import Animals
from animals.forms import AnimalsForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404


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


class AnimalsUpdate(UpdateView):
    model = Animals
    template_name = 'animals/animals_edytuj.html'
    form_class = AnimalsForm
    success_url = '/animals/'
    fields = ('oznaczenie', 'typ', 'old', 'weight', 'price', 'user')
    queryset = Animals.objects.all()
    def get_object(self, queryset=None):
        obj = Animals.objects.get(pk=self.kwargs['pk'])
        return obj
    # def get_object(self):
        # return Animals.objects.get(pk=self.request.GET.get('pk'))
    def form_valid(self, form):
        form.save()
        return super(AnimalsUpdate, self).form_valid(form)