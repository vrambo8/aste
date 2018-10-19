from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class UtenteLoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    def clean(self):
        username=self.cleaned_data('username')
        password=self.cleaned_data('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active():
            raise ValidationError(_("Invalid username or password, please check and try again"), code="invalid login")
        if username.length>20:
            raise ValidationError(_("Username can be only 20 characters long"),code="max_length username")
        if username is None:
            raise ValidationError(_("Please insert your username"), code="null username")
         
        return self.cleaned_data
    

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Optional. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )