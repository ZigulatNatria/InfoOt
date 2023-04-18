from django.forms import ModelForm
from django import forms

from .models import Employee





class EmployeeAddForm(ModelForm):
    # name = forms.CharField(max_length=100,
    #                        label='Правообладатель фильма',
    #                        widget=forms.TextInput
    #                        (attrs={'placeholder': 'не более 100 символов '})
    #                        )

    class Meta:
        model = Employee
        fields = [
            'surname',
            'name',
            'patronym',
            'birth_date',
            'phone',
            'subdivision',
            'photo_employee',
            'profession'
        ]
