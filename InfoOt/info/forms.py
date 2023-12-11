from django.forms import ModelForm
from django import forms

from .models import Employee, Certificate, Education, MedicineParagraph, Passport, \
    Medicine, Psycho, Sawc, Order, Instruction


class EmployeeAddForm(ModelForm):
    # name = forms.CharField(max_length=100,
    #                        label='Правообладатель фильма',
    #                        widget=forms.TextInput
    #                        (attrs={'placeholder': 'не более 100 символов '})
    #                        )

    class Meta:
        model = Employee
        # fields = ('__all__')
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
        ]

        widgets = {
            'username': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Username',
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
                    "placeholder": 'Имя',
                }
            ),

            'name': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Отчество',
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

            'profession': forms.Select(
                attrs={
                    "class": "form-select",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Подразделение',
                }
            ),
        }



class CertificateAddForm(ModelForm):

    class Meta:
        model = Certificate
        fields = [
            'name_certificate',
            'date_finish_certificate',
            'date_end_certificate',
            'certificate',
            'protocol',
            'employee'
        ]


class EducationAddForm(ModelForm):

    class Meta:
        model = Education
        fields = [
            'prof_name',
            'date_finish_education',
            'document_education',
            'employee'
        ]

        widgets = {
            'prof_name': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Название обучения',
                }
            ),

            'date_finish_education': forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Дата обучения',
                }
            ),

            'document_education': forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Документ об образовании',
                }
            ),

            'employee': forms.Select(
                attrs={
                    "class": "form-select",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Работник',
                }
            ),
        }


class MedicineParagraphAddForm(ModelForm):

    class Meta:
        model = MedicineParagraph
        fields = [
            'number_paragraph',
            'date_finish_paragraph',
            'date_end_paragraph',
            'medicine'
        ]

        widgets = {
            'number_paragraph': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Номер пункта',
                }
            ),

            'date_finish_paragraph': forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Дата осмотра',
                }
            ),

            'date_end_paragraph': forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Срок действия',
                }
            ),

            'medicine': forms.Select(
                attrs={
                    "class": "form-select",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Заключение',
                }
            ),
        }


class PassportAddForm(ModelForm):

    class Meta:
        model = Passport
        fields = [
            'series',
            'number',
            'date_of_issue',
            'fms',
            'registration',
            'employee'
        ]


class MedicineAddForm(ModelForm):

    class Meta:
        model = Medicine
        fields = [
            'document_medicine',
            'date_medicine',
            'employee'
        ]

        widgets = {
            'document_medicine': forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Заключение',
                }
            ),

            'date_medicine': forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Дата заключения',
                }
            ),

            'employee': forms.Select(
                attrs={
                    "class": "form-select",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Работник',
                }
            ),
    }


class PsychoAddForm(ModelForm):

    class Meta:
        model = Psycho
        fields = [
            'document_psycho',
            'date_finish_psycho',
            'date_end_psycho',
            'employee'
        ]


class SawcAddForm(ModelForm):

    class Meta:
        model = Sawc
        fields = [
            'name_profession',
            'name_subdivision',
            'number_card',
            'date_card',
            'document_sawc',
        ]


class SawcAddToEmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = [
            'sawc',
        ]


class OrderAddForm(ModelForm):

    class Meta:
        model = Order
        fields = [
            'name',
            'number',
            'date',
            'file',
            'employees',
        ]


class InstructionFormAdd(ModelForm):

    class Meta:
        model = Instruction
        fields = [
            'number',
            'name',
            'date',
            'date_end',
            'file',
            'profession',
            'employee',
        ]