from distutils.log import error
import email
from django import forms
from .models import Coach

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