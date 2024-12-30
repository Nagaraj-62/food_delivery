from django import forms
from .models import User_details
from django.contrib.auth.hashers import make_password


class RegForm(forms.ModelForm):
    class Meta:
        model=User_details
        fields=['username','phone_number','email','first_name','last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
        def save(self):
            user = super().save(commit=False)
            user.password = make_password(self.cleaned_data['password'])
            user.save()
            return user 
        
class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())