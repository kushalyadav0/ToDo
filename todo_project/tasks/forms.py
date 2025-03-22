from .widgets import DateTimePickerInput
from django import forms
from .models import Tasks

class task_form(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'

        widgets = {
            'deadline':DateTimePickerInput()
        }