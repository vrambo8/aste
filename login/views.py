from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from .forms import *
from django.db import transaction



# Create your views here.

def register(request):
    if request.method == "POST":
        uform= UserForm(data= request.POST)
        pform= ProfileForm(data= request.POST)
        if uform.is_valid() and pform.is_valid():
            user=uform.save()
            user.refresh_from_db()
            pform=ProfileForm(request.POST, instance= user.profile)
            pform.full_clean()
            pform.save()
            password = uform.cleaned_data.get('password'), 
            user=authenticate(username=user.username, password=password)
            login(request, user)
            return redirect('feed')
        else:
            print(uform.errors, pform.errors)
    else:
        uform= UserForm()
        pform=ProfileForm()
        
    return render(request, 'registration/registration.html', {'uform': uform, 'pform': pform})


        

    
        