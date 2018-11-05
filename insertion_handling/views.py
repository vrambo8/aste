from django.shortcuts import render, redirect
from insertion_handling.models import InsertionForm
from django.contrib.auth.decorators import login_required
from feed.models import Inserzione

# Create your views here.
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
    if (request.method=="POST"):
        print(ins.titolo)
        form=InsertionForm(data=request.POST, instance=ins)
        if form.is_valid():
            form.save()
            
            return redirect('feed')
        else: print(form.errors)
        
    else: form=InsertionForm(instance=ins)
    return render(request, 'update_insertion.html', {'form': form})