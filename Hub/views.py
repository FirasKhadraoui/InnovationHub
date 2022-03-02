from django.http import HttpResponse
from django.shortcuts import render
from .models import Coach

# Create your views here.
def HomePage(request):
    return HttpResponse("<h1>Welcome To ...</h1>")

def ListCoach(request):
    List=Coach.objects.all() # select * from coach
    return render( # 3 paramétres
        request,
        'Hub/list.html', # page à afficher
        {
            'list_Coach':List
        } 
    )