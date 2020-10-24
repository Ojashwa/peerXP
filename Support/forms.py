from django import forms
from django.forms import ModelForm
from.models import Userlogin

class UserloginForms(forms.ModelForm):
    class Meta:
        modal = Userlogin
        fields = ['name','email','password']
