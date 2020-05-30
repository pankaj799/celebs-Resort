from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class UserForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Name'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Phone'
            }),
            'no_of_child': forms.TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Number Of Children'
            }),
            'no_of_adult': forms.TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Number Of Adults'
            }),
            'check_in': forms.SelectDateWidget(),
            'check_out': forms.SelectDateWidget(),
        }
