from django.db import models
from django import forms
from feed.models import Inserzione
from django.core.exceptions import ValidationError
# Create your models here.

class InsertionForm(forms.ModelForm):
    def clean(self):
        cleaned_data=super(InsertionForm, self).clean()
        titolo=cleaned_data.get('titolo')
        descrizione=cleaned_data.get('descrizione')
        indirizzo=cleaned_data.get('indirizzo')
        max_prezzo=cleaned_data.get('max_prezzo')
        
        validators=[]
        
        if len(titolo)<10:
            validators.append(ValidationError(_("Title must be at least 10 characters long"), code="insufficient title length"))
        if max_prezzo<=0:
            validators.append(ValidationError(_("Price must be greater than 0"), code="negative max_prezzo"))
        if validators:
            raise ValidationError(validators)
        return self.cleaned_data

    class Meta:
        model=Inserzione
        fields=['titolo', 'descrizione', 'indirizzo', 'max_prezzo', 'immagine']