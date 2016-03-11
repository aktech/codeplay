from django import forms


class NameForm(forms.Form):
    lang = forms.CharField(label='Language', max_length=100)
    code = forms.CharField(widget=forms.Textarea)
