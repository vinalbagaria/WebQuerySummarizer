from django import forms

class NameForm(forms.Form):
    queryy = forms.CharField(label='Query', max_length=100)