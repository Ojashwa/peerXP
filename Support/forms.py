from django import forms
from django.forms import ModelForm
from.models import Userlogin

class UserloginForms(forms.ModelForm):
    '''registration form of modal class'''
    class Meta:
        modal = Userlogin
        fields = ['name','email','password']
class TokenForm(forms.Form):
    '''token form '''
    Department = forms.CharField(max_length=200)
    Category = forms.CharField(max_length=200)
    PWSLab_Project_URL = forms.CharField(max_length=200)
    Subject = forms.CharField(max_length=150)
    Description = forms.CharField(max_length=150)
    Contact_Name = forms.CharField(max_length=100)
    Email = forms.CharField(max_length=100)
    Priority = forms.CharField(max_length=100)
