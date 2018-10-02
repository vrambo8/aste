from django.db import models
from shortuuid import *
# Create your models here.
class Inserzione (models.Model):
    titolo=models.CharField(max_length=50)
    uuid=ShortUUID()
    id=models.CharField(max_length=30, primary_key=True, default=uuid.uuid())
    descrizione=models.CharField(max_length=500)
    venditore=models.ForeignKey('Utente', on_delete=models.CASCADE, related_name="venditore")
    utente=models.ManyToManyField('Utente', related_name="utente")
    indirizzo=models.CharField(max_length=50)
    prezzo=models.IntegerField()
    class Meta:
        unique_together=('titolo', 'id')
    def __str__(self):
        return self.titolo
    

class Utente (models.Model):
    username=models.CharField(max_length=20)
    nome=models.CharField(max_length=50)
    cognome=models.CharField(max_length=100)
    dataNascita=models.DateField
    email=models.EmailField()
    password=models.CharField(max_length=20)
    class Meta:
        unique_together=('username','email')
    def __str__(self):
        return self.username
        

    

    
    
    
    