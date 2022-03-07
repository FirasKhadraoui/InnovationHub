from django import forms
from .models import Coach
from django.contrib.auth.models import User  #User de django pas notre user de .models
from django.contrib.auth.forms import UserCreationForm

class CoachForm(forms.Form):
    first_name=forms.CharField(
        label='Prenom',
        max_length=50
    )
    last_name=forms.CharField()
    email=forms.EmailField()

class CoachModelForm(forms.ModelForm):
    class Meta:
        model= Coach
        fields = '__all__' #['last_name',] #spécifie
        #exclude=[] # sauf ceci
        error_message={
            'last_name':{
                'max_length':"Name too long !!!"
            }
        }

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email']    #'__all__'
        