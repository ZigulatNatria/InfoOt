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
            'department',
            'photo_employee',
            'profession',
            'supervisor',
            'password1',
            'password2',
        ]

        widgets = {
            'username': forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Email',
                }
            ),

            'surname': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Фамилия',
                }
            ),

            'patronym': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Отчество',
                }
            ),

            'name': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Имя',
                }
            ),

            'phone': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Телефон',
                }
            ),

            'birth_date': forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Дата рождения',
                }
            ),

            'photo_employee': forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Фото работника',
                }
            ),

            'subdivision': forms.Select(
                attrs={
                    "class": "form-select",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Подразделение',
                }
            ),

            'department': forms.Select(
                attrs={
                    "class": "form-select",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Отдел',
                }
            ),

            'profession': forms.Select(
                attrs={
                    "class": "form-select",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Подразделение',
                }
            ),

            # 'password1': forms.PasswordInput(
            #     attrs={
            #         "class": "form-control",
            #         "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
            #         "placeholder": 'Пароль',
            #     }
            # ),
            #
            # 'password2': forms.PasswordInput(
            #     attrs={
            #         "class": "form-control",
            #         "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
            #         "placeholder": 'Подтверждение пароля',
            #     }
            # ),
        }
