from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from info.models import Employee
from django import forms
from django.forms import ModelForm


class UserAddForm(UserCreationForm):

    class Meta:
        model = Employee
        fields = [
            'username',
            'surname',
            'name',
            'patronym',
            'birth_date',
            'phone',
            'subdivision',
            'photo_employee',
            'profession',
            'supervisor',
            'password1',
            'password2',
        ]