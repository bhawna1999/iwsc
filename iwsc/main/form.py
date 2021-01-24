from django import forms
from .models import Contact
from phonenumber_field.formfields import PhoneNumberField
from django.forms.utils import ValidationError
from django.core.validators import RegexValidator
from django.core import validators


numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')

class ContactForm(forms.ModelForm):
    message= forms.CharField(required=True,widget=forms.Textarea(attrs={'rows': 4,'cols':23}))
    class Meta:
        model = Contact
        fields = [
            'name',
            'mail',
            'contact_Number',
            'message']
    def clean(self):
        name=self.cleaned_data.get("name")
        if (name.isdigit()) :
            raise forms.ValidationError("Name should not contain digit")

        

