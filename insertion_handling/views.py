from django.shortcuts import render, redirect
from insertion_handling.models import InsertionForm
from django.contrib.auth.decorators import login_required
from feed.models import Inserzione
from django.contrib import messages
# Create your views here.
def inserzione(request, ins_id):
    ins=Inserzione.objects.get(id=ins_id)
    offerenti=ins.offerenti
    interessati=ins.interessati
    user=request.user.profile
    allowed= ins.venditore==user
    if request.method=='POST':
        if 'interested' in request.POST:
            interessati.add(user)
            redirect('inserzione', ins_id=ins_id)
        if 'uninterested'in request.POST:
            interessati.remove(user)
            redirect('inserzione', ins_id=ins_id)
    context= {
        'ins': ins,
        'offerenti' : offerenti.all(),
        'interessati' : interessati.all(),
        'user': user,
        'allowed': allowed
        
        }
    return render(request, 'inserzione.html', context)

@login_required
def new_insertion(request):
    if (request.method=="POST"):
        form=InsertionForm(request.POST)
        if form.is_valid():
            ins=form.instance
            ins.venditore=request.user.profile
            form.save()
            
            return redirect('feed')
        else: print(form.errors)
        
    else: form=InsertionForm()
    return render(request, 'new_insertion.html', {'form': form } )

@login_required
def update_insertion(request, ins_id):
    ins=Inserzione.objects.get(id=ins_id)
    allowed= ins.venditore==request.user.profile
    if (request.method=="POST"):
        form=InsertionForm(data=request.POST, instance=ins)
        if form.is_valid():
            form.save()
            
            return redirect("inserzione", ins_id=ins_id)
        
    else: 
        if allowed:
            form=InsertionForm(instance=ins)
        else:
            messages.error(request, "Sorry, you don't have access to this insertion.")
            return redirect("inserzione", ins_id=ins_id)
    return render(request, 'update_insertion.html', {'form': form, 'ins': ins})

def interested(request, ins_id):
    user=request.user.profile
    ins=Inserzione.objects.get(id=ins_id)
    if (request.method=="POST"):
        ins.interessati.append(user)
    return redirect("inserzione", ins_id=ins_id)
        
        