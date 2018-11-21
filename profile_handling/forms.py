from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


class UtenteLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
       
    def clean(self):
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        
        validators=[]
        if not user or not user.is_active:
            validators.append(ValidationError(_("Invalid username or password, please check and try again"), code="invalid profile_handling"))
        if len(username)>20:
            validators.append(ValidationError(_("Username can be only 20 characters long"),code="max_length username"))
        if username is None:
            validators.append(ValidationError(_("Please insert your username"), code="null username"))
        if validators:
            raise ValidationError(validators)
        login(self.request, user)
        return self.cleaned_data
    

