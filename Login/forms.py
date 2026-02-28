from django import forms
from .models import UserRegistration,Designation

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=UserRegistration
        fields='__all__'
