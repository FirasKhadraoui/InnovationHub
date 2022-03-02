from django.http import HttpResponse
from django.shortcuts import render
from .models import Coach, Projet

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

def details_coach(request,id):
    coach=Coach.objects.get(id=id)
    return render( 
        request,
        'Hub/details.html',
        {
            'coach': coach
        } 
    )

def list_project(request) :
    list= Projet.objects.all()
    return render(
        request,
        'Hub/project_list.html',
        {
            'list_project':list
        }
    )

# class ProjectListView(ListView) :
#     model=Projet
#     template_name='Hub/projet_list.html'