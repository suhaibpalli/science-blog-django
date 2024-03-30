from django.contrib import admin
from .models import Experiment

class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty_level', 'subject', 'created_on')
    list_filter = ('subject',)  
    search_fields = ['name', 'subject']


admin.site.register(Experiment, ExperimentAdmin)
