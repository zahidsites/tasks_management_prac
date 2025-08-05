from django import forms
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
class CustomRegiForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    confirm_pass = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','confirm_pass']

    def clean_email(self):
        email = self.cleaned_data['email']
        email_exist = User.objects.filter(email=email).exists()

        if email_exist:
            raise forms.ValidationError("Email already exists try another email")
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if len(password1) < 4:
            raise forms.ValidationError("Password lenth should be more than 3 letters")
        return password1
    
    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('password1')
        pass2 = cleaned_data.get('confirm_pass')
        print(pass2,pass1)
        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError("Password does not match")
        return cleaned_data

        
        
        
