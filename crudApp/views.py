from django.shortcuts import render,redirect
from .Forms import patienForm
from django.contrib import messages
from django.http import HttpResponse
from .models import patient
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.

@login_required
def patient_create(request):
    if request.method == 'POST':
        form = patienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list')
    else:
        form = patienForm()
    return render(request,'patient_form.html',{'form':form})

@login_required
def patient_list(request):
    patients = patient.objects.all()
    return render(request,'patient_list.html',{'patients':patients})

@login_required
def update_patient(request,pk):
    patient = get_object_or_404(patient,pk=pk)
    
    if request.method == 'POST':
        form = patienForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            
            return redirect('/list')
        
    else:
        form = patienForm(instance=patient)
        
    return render(request,'patient_form.html',{'form':form})
    
@login_required
def delete_patient(request,pk):
    patients = get_object_or_404(patient,pk=pk)
    if request.method =='POST':
        patients.delete()
        return redirect ('/list')
    return render(request,'patient_delete.html',{'patient':patients})

def user_login(request):
    if request.method == 'POST':
        form - AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/list')
        else:
            form =AuthenticationForm()
        return render(request,'registration/login.html',{'form':form})



def user_logout(request):
    logout(request)
    return redirect('/accounts/login')

