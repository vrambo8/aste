from __future__ import unicode_literals
from shortuuid import ShortUUID


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Inserzione (models.Model):
    titolo=models.CharField(max_length=50)
    uuid=ShortUUID()
    id=models.CharField(max_length=30, primary_key=True, unique=True, default=uuid.uuid())
    descrizione=models.CharField(max_length=500, default='')
    venditore=models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="venditore", blank=False)
    interessati=models.ManyToManyField('Profile', related_name="interessati", default=[])
    offerenti=models.ManyToManyField('Profile', related_name="offerenti", default=[])
    indirizzo=models.CharField(max_length=50, blank=False)
    max_prezzo=models.IntegerField(blank=False)
    
    class Meta:
        verbose_name=_('insertion')
        verbose_name_plural=_('insertions')
    def __str__(self):
        return self.titolo
    

class Profile (models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    partita_iva=models.CharField(max_length=50)
    luogo=models.CharField(max_length=50, blank=True)
    
    class Meta:
        verbose_name=_('user')
        verbose_name_plural=_('users')
        
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile( sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
@receiver(post_save, sender=User)
def save_user_profile( sender, instance, **kwargs):
            instance.profile.save()
        
    
        

    

    
    
    
    