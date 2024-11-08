from django import forms
from django.core import validators

def check_for_a(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError("Name needs to start with a")

class FormName (forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(5)])
    # name = forms.CharField(validators=[check_for_a])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Input your email again")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Make sure email match!")
    