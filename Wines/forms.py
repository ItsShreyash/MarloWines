from django import forms
from .models import CustomUser
from .models import ContactUs

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = {'name','Useremail','password'}

class CustomContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = {'name','email','message'}
