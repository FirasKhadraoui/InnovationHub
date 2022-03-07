from django.http import HttpResponse
from django.shortcuts import redirect, render
from Hub.forms import CoachForm, CoachModelForm
from .models import Coach, Projet, Student
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse

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

#3éme méthode par contrainte
def Coach_addModelForm(request):
    form= CoachModelForm()
    if request.method=="POST":
        form= CoachModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Hub_Coach_list')

    return render(request,'Hub/Coach_add.html',
{
'form':form,
}
)

#Class
class CoachCreateView(CreateView):
    model= Coach
    form_class = CoachModelForm
    template_name="Hub/Coach_add.html"
    #Par défaut template_name="{model}_form.html" #Create & Update
    def get_success_url(self):
        return reverse('Hub_Coach_list')  # Redirection

class CoachUpdateView(UpdateView):
    model=Coach
    form_class=CoachModelForm
    template_name="Hub/Coach_add.html"
    # success_url = 
    def get_success_url(self):
        return reverse('Hub_Coach_list')

class CoachDeleteView(DeleteView):
    model=Coach
    def get_success_url(self):
        return reverse('Hub_Coach_list')

#2éme méthode suppression sans comfirm_delete
def delete_coach(request,id):
    st=Student.objects.get(pk=id)
    st.delete()
    return redirect ('student_list')


################  Students ################
def ListStudent(request):
    List=Student.objects.all()
    return render(
        request,
        'Hub/list_student.html',
        {
            'list_Student':List
        } 
    )

def details_student(request,id):
    student=Student.objects.get(id=id)
    return render( 
        request,
        'Hub/details_student.html',
        {
            'student': student
        } 
    )