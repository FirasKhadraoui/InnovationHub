from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class User(models.Model):
    fname = models.CharField(verbose_name="First Name",max_length=10)
    lname = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="Email",null=False)
    def __str__(self):
        return f"{self.fname} _ {self.lname}"
    

class Student(User):
    pass

class Coach(User) :
    # def get_absolute_url(self):
    #     return redirect()
    pass

class Projet(models.Model):
    project_name= models.CharField(
        verbose_name="Titre du projet",max_length=50)
    project_duration = models.IntegerField(
        verbose_name="Durée Estimée",default=0)
    time_allocated = models.IntegerField(
        verbose_name="Temps Alloué",
        validators=[
            MinValueValidator(1,'The minimum Value required is 1'),
            MaxValueValidator(10,'The maximum Value required is 10')
        ])
    needs = models.TextField(
        verbose_name="Besoins",max_length=250)
    desciption = models.TextField(max_length=250)
    isValid = models.BooleanField(default=False)
    
    creator = models.OneToOneField ( #OneToOne
        Student,
        on_delete=models.CASCADE,
        related_name="Project_Owner",
        null=True
    )

    supervisor = models.ForeignKey( #OneToMany
        to = Coach,
        on_delete=models.SET_NULL,
        blank=True,#required par rapport formulaire
        null=True,#required par rapport BD
        related_name="project_Coach" 
    )

    members=models.ManyToManyField(
        to=Student,
        blank=True,
        related_name="Les_membres", #ManyToMany related_name obligatoire
        through="MembershipInProjects",
        
    )
    def __str__(self):
        return f"{self.project_name}"

class MembershipInProjects(models.Model):
    project=models.ForeignKey(
        to= Projet,
        on_delete=models.CASCADE
    )
    student=models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    time_allocated = models.IntegerField()
    def __str__(self) :
        return f"{self.project}"
    class Meta:
        verbose_name_plural="MemberShip" #Changer le nom dans le sidebar