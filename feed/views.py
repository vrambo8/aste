from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import *
from insertion_handling import views

# Create your views here.
def home_page(request):
    utente=request.user
    context= {
        'utente' : utente
        }
    return render(request, 'home.html', context)

@login_required
def page(request):
   
    ins_lista=Inserzione.objects.all()
    paginator = Paginator(ins_lista, 50)
    
    page = request.GET.get('page')
    inserzioni=paginator.get_page(page)
    context= {
        'inserzioni' : inserzioni
        }
    return render(request,'page.html', context)


    
    
    
    