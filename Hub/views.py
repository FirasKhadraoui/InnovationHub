from django.http import HttpResponse
from django.shortcuts import redirect, render
from Hub.forms import CoachForm, CoachModelForm
from .models import Coach, Projet
from django.views.generic import CreateView, UpdateView

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

def Coach_add(request):
    #print(request.POST)
    if request.method=="POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')

        Coach.objects.create(
            fname=firstName,
            lname= lastName,
            email=email
        )
        return redirect('Hub_Coach_list')

    return render(request,'Hub/Coach_add.html')

#2éme méthode (forms.py)
def Coach_addForm(request):
    form= CoachForm()
    if request.method=="POST":
        form= CoachForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data.get('first_name')
            lastName = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')

        Coach.objects.create(
            fname=firstName,
            lname= lastName,
            email=email
        )
        #Coach.objects.create(**form.cleaned_data) #Remplace elli 9ablou (spread operator)
        return redirect('Hub_Coach_list')

    return render(request,'Hub/Coach_add.html',
{
'form':form,
}
)
