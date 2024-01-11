from django import forms
from .models import Employee


class PdfTestForm(forms.Form):
    text = forms.CharField(max_length=255)
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())