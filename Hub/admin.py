from django.contrib import admin, messages
from Hub.models import Coach, MembershipInProjects, Projet, Student, User

# Register your models here.
#Student
class ProjectInline(admin.StackedInline): #TabularInline n'est pas responsive
    model=Projet
    # fieldsets=[
    #     (
    #         None,
    #         {
    #             'fields':['project_name']
    #         }
    #     )
    # ]
class StudentAdmin(admin.ModelAdmin):
    list_display=(
        'lname',
        'fname',
        'email'
    )
    fields=(
        ('lname','fname'),
        'email'
    )
    search_fields=['fname','lname'] #Search with first name & last name
    inlines=[
        ProjectInline,
    ]
admin.site.register(Student, StudentAdmin)

#Coach with another method
@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display=(
        'lname',
        'fname',
        'email'
    )
    fields=( 
        ('lname','fname'), #Affichage 2 champs dans mm ligne
        'email'
    )

class ProjectDurationFilter(admin.SimpleListFilter): #Créer un filter personnalisé sur la durée
    title='Durée' #Affichage
    parameter_name='project_duration' #Mm nom dans le projet(Liaison avec le modéle)

    def lookups(self,request,model_admin):
        return(
            ('1 month',('less than a month')),
            ('3 month',('less than 3 month')),
        )

    def queryset(self,request,queryset):
        if self.value()=='1 month':
            return queryset.filter(project_duration__lte=30)  #Select * from Project where pD<=30
        if self.value()=='3 month':
            return queryset.filter(project_duration__lte=90, project_duration__gte=30)

def set_valid(modeladmin,request,queryset):
    
    rows = queryset.update(isValid = True)
    if rows == 1:
        message = '1 project was'
    else:
        message = f'{rows} projects were'
    messages.success(request,message=f'{message} marked as valid')

set_valid.short_description="Validate"

class ProjectAdmin(admin.ModelAdmin):
    def set_invalid(modeladmin,request,queryset):
        rows_invalid=queryset.filter(isValid=False)
        if rows_invalid.count()>0:
            messages.error(request,message=f'{rows_invalid.count()} are already marked as invalid')
        else:
            rows = queryset.update(isValid = False)
            if rows == 1:
                message = '1 project was'
            else:
                message = f'{rows} projects were'
            messages.success(request,message=f'{message} marked as invalid')

    # def set_invalid(modeladmin,request,queryset):
    #     rows = queryset.update(isValid = False)
    #     if rows == 1:
    #         message = '1 project was'
    #     else:
    #         message = f'{rows} projects were'
    #     messages.success(request,message=f'{message} marked as invalid')


    set_invalid.short_description="Refuse"
    actions=[set_valid,'set_invalid']
    actions_on_bottom= True
    actions_on_top= True

    
    list_display=(
        'project_name',
        'project_duration',
        'creator',
        'supervisor'
    )
    #date_hierarchy= 'updated_at' #Trier par la date 
    autocomplet_fields=['supervisor'] #autocomplet f recherche
    fieldsets= [
        (
            'Etat',
            {
                'fields':['isValid','time_allocated']
            }
        ),
        (
            'About',
            {
                'classes': ('collapse',),
                'fields':['project_name', ('creator', 'supervisor')]
            }
        )
    ]
    empty_value_display='-empty-'
    #radio_fields={"supervisor":admin.VERTICAL} #Utiliser le radio
    list_filter=(
        'creator',
        'isValid',
        ProjectDurationFilter
    )

admin.site.register(Projet,ProjectAdmin)
admin.site.register(User)
admin.site.register(MembershipInProjects)