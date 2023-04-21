from django.forms import ModelForm
from django import forms

from .models import Employee, Certificate, Education, MedicineParagraph, Passport, Medicine


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


class MedicineParagraphAddForm(ModelForm):

    class Meta:
        model = MedicineParagraph
        fields = [
            'number_paragraph',
            'date_finish_paragraph',
            'date_end_paragraph',
            'medicine'
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