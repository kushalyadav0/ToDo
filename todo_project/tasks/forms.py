from django import forms 
from django.forms import ModelForm
from .models import tasks

class task_form(forms.ModelForm):
    class Meta:
        model = tasks
        fields = ('task_name', 'task_description', 'complete', )