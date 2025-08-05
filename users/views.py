from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from users.forms import CustomRegiForm
from django.contrib import messages
# Create your views here.
def sign_up(request):
    form = CustomRegiForm()
    if request.method == 'POST':
        form = CustomRegiForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            messages.success(request,"success")
    
    return render(request,'signup.html',{'form':form})

def signIn(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pass1 = request.POST['password1']
        print(uname,pass1)
        user = authenticate(request, username=uname, password=pass1)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
            
    return render(request,'signin.html')

def logOut(request):
    if request.method == 'POST':
        logout(request)
        return redirect('signin')
