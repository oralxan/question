from django import forms

class EmailForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
