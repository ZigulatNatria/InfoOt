from django import forms


class PdfTestForm(forms.Form):
    text = forms.CharField(max_length=255)