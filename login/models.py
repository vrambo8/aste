from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from feed.models import User, Profile
from django import forms


class UserForm(forms.ModelForm):
    password2=forms.CharField(max_length=30, label="Confirm Password")
    
    def clean(self):
        cleaned_data=super(UserForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        username = cleaned_data.get("username")
        
        def hasNumbers(str):
            return any(char.isdigit() for char in str)
        
        validators=[]
        
        if len(username)>20 or len(username)<8:
            validators.append(ValidationError(_("Username needs to be 8 to 20 characters long"),code="length username"))
        if len(password)>20 or len(password)<8:
            validators.append(ValidationError(_("Password needs to be 8 to 20 characters long"),code="length password"))
        if not hasNumbers(password):
            validators.append(ValidationError(_("Password needs to contain at least one digit"), code="missing digit password"))
        if (password!=password2):
            validators.append(ValidationError(_("Passwords do not match"), code="unmatching passwords"))
        
        raise ValidationError(validators)
        return self.cleaned_data
    
    class Meta:
        model = User
        help_texts = {
            'username': 'Range from 8 to 20 characters',
            'password': 'Range from 8 to 20 characters, needs to contain at least a digit'}
        fields= ["username", "email", "password", "password2"]
        
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ["partita_iva", "luogo"]
        
