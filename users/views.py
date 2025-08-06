from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from users.forms import CustomRegiForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.tokens import default_token_generator
# Create your views here.
def sign_up(request):
    form = CustomRegiForm()
    if request.method == 'POST':
        form = CustomRegiForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active = False
            user.save()
            messages.success(request,"success")
    
    return render(request,'signup.html',{'form':form})

def signIn(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
            
    return render(request,'signin.html',{'form':form})

def logOut(request):
    if request.method == 'POST':
        logout(request)
        return redirect('signin')


def user_activate(request,user_id,token):
    try:
        user = User.objects.get(id = user_id)
         
        if default_token_generator.check_token(user,token):

            user.is_active = True
            user.save()
            return redirect('signin')
        else:
            return HttpResponse("User Id Invalid")
    except User.DoesNotExist:
        return HttpResponse("User Not found")
