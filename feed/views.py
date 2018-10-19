from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *

# Create your views here.
def home_page(request):
    utente=User.objects.get(username="vitto")
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

def inserzione(request, ins_id):
    ins=Inserzione.objects.get(id=ins_id)
    offerenti=ins.offerenti.all()
    print(offerenti)
    interessati=ins.interessati.all()
    context= {
        'ins': ins,
        'offerenti' : offerenti,
        'interessati' : interessati
        }
    return render(request, 'inserzione.html', context)
    
    
    
    