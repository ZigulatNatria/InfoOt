from django.forms import ModelForm
from django import forms

from .models import Employee, Certificate, Education, MedicineParagraph, Passport, \
    Medicine, Psycho, Sawc, Order, Instruction


class EmployeeAddForm(ModelForm):

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
                    "placeholder": 'Профессия',
                }
            ),
        }


class CertificateAddForm(ModelForm):

    class Meta:
        model = Certificate
        fields = [
            'name_certificate_list',
            'date_finish_certificate',
            'date_end_certificate',
            'certificate',
            'protocol',
            'employee'
        ]

        widgets = {
            # 'name_certificate': forms.TextInput(
            #     attrs={
            #         "class": "form-control",
            #         "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
            #         "placeholder": 'Название обучения',
            #     }
            # ),

            'name_certificate_list': forms.Select(
                attrs={
                    "class": "form-select",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Название обучения',
                }
            ),

            'date_finish_certificate': forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Дата обучения',
                }
            ),

            'date_end_certificate': forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Срок действия',
                }
            ),

            'certificate': forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Удостоверение',
                }
            ),

            'protocol': forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Протокол',
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


class CertificateCheckForm(CertificateAddForm):
    class Meta:
        model = Certificate
        fields = [
            'application',
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
            'number_paragraph_list',
            'date_finish_paragraph',
            'date_end_paragraph',
            'medicine'
        ]

        widgets = {

            'number_paragraph_list': forms.Select(
                attrs={
                    "class": "form-select",
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


class MedicineParagraphCheckForm(MedicineParagraphAddForm):
    class Meta:
        model = MedicineParagraph
        fields = [
            'application',
        ]


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

        widgets = {
            'document_psycho': forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Заключение',
                }
            ),

            'date_finish_psycho': forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Дата заключения',
                }
            ),

            'date_end_psycho': forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Срок действия',
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


class PsychoCheckAddForm(PsychoAddForm):

    class Meta:
        model = Psycho
        fields = [
            'application',
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

        widgets = {
            'name_profession': forms.Select(
                attrs={
                    "class": "form-select",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Профессия',
                }
            ),

            'name_subdivision': forms.Select(
                attrs={
                    "class": "form-select",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Подразделение',
                }
            ),

            'number_card': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Номер карты',
                }
            ),

            'date_card': forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Дата карты СОУТ',
                }
            ),

            'document_sawc': forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Карта СОУТ',
                }
            ),
        }


class SawcAddToEmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = [
            'sawc',
        ]

        widgets = {
            'sawc': forms.Select(
                attrs={
                    "class": "form-select",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Карта СОУТ',
                }
            ),
        }


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