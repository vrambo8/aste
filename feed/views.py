from django.shortcuts import render
from django.core.paginator import *
from .models import *
from django.core import paginator

# Create your views here.
def home_page(request):
    utente=Utente.objects.get(username="BITCH")
    context= {
        'utente' : utente
        }
    return render(request, 'home.html', context)

def page(request):
   
    ins_lista=Inserzione.objects.all()
    paginator = Paginator(ins_lista, 50)
    
    page = request.GET.get('page')
    inserzioni=paginator.get_page(page)
    context= {
        'inserzioni' : inserzioni
        }
    return render(request,'page.html', context)


    
    
    