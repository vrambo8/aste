from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_location', 'get_partita')
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
    
    def get_location(self, instance):
        return instance.profile.luogo
    get_location.short_description = 'Location'
    
    def get_partita(self, instance):
        return instance.profile.partita_iva
    get_partita.short_description = 'Partita IVA'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Inserzione)
