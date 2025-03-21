from django import forms
from .models import Tasks

class task_form(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'