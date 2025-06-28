from .widgets import DateTimePickerInput
from django import forms
from .models import Tasks

class task_form(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ['user',]
        widgets = {
            'deadline':DateTimePickerInput()
        }

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']