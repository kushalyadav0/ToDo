# for widgets 
from django import forms
#DateTimePicker
class DateTimePickerInput(forms.DateTimeInput):
    input_type='datetime'
    # this will be imported in forms.py and and can be used there in DateTimeField.