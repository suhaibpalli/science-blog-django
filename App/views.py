from django.shortcuts import render
from .models import Experiment
from django.views import generic

# Create your views here.

class ExperimentList(generic.ListView):
    model = Experiment
    queryset = Experiment.objects.filter(difficulty_level__in=[1, 2, 3, 4, 5]).order_by('-created_on')
    template_name = 'index.html'


class DetailView(generic.DetailView): 
    model = Experiment
    template_name = 'experiment_detail.html'
    
    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        queryset = queryset.filter(pk=self.kwargs['pk'])
        obj = queryset.get()
        return obj
