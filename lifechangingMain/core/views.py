from django.shortcuts import render, redirect
from .forms import *  
from .models import * 

# Create your views here.
def index(request):
    return render(request, 'index.html')



def donor(request):
    if request.method == 'POST': 
        form = T_donorForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            return redirect('contrib')  
        else:
            print("Form is not valid")  
    else:
        form = T_donorForm()  
    return render(request, 'donor.html', {'form': form}) 

def contrib(request):
    t_contrib = T_donor.objects.all()
    p_contrib = P_donor.objects.all()
    return render(request, 'contributors.html', {'t_contrib': t_contrib, 'p_contrib': p_contrib})

def groupcontrib(request):
    if request.method == 'POST': 
        groupcontribform = P_donorForm(request.POST, request.FILES)  
        if groupcontribform.is_valid():  
            groupcontribform.save()  
            return redirect('contrib')  
        else:
            print("Form is not valid")  
    else:
        groupcontribform = P_donorForm()  
    return render(request, 'group_contributor.html', {'groupcontribform': groupcontribform}) 