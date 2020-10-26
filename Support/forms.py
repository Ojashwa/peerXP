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
    category = forms.CharField(max_length=200)
    webUrl = forms.CharField(max_length=200)
    subject = forms.CharField(max_length=150)
    description = forms.CharField(max_length=150)
    email = forms.CharField(max_length=100)
    priority = forms.CharField(max_length=100)
    departmentId = forms.CharField(max_length=200)
    contactId = forms.CharField(max_length=200)

