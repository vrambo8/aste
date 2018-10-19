from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from .models import *

class UtenteLoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UtenteLoginForm, self).__init__(*args, **kwargs)
    def get_user(self): 
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        return user
       
    def clean(self):
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise ValidationError(_("Invalid username or password, please check and try again"), code="invalid login")
        if len(username)>20:
            raise ValidationError(_("Username can be only 20 characters long"),code="max_length username")
        if username is None:
            raise ValidationError(_("Please insert your username"), code="null username")
         
        return self.cleaned_data
    

