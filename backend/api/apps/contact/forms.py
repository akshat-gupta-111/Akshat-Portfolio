from django import forms
from django.core.validators import EmailValidator
# Create your models here.
class Contact(forms.Form):
    uname = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    phone = forms.CharField(max_length=15)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    def __str__(self):
        return self.email