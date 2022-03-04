import imp
from django.urls import path
from .views import Coach_add, Coach_addForm, CoachCreateView, HomePage, ListCoach, ListStudent, details_coach, details_student, list_project


urlpatterns=[
    path('home',HomePage,name="Hub_home"),
    path('listCoach',ListCoach,name="Hub_Coach_list"),
    #path('Coach',details_coach,name="Hub_Coach_details"), #id statique dans la fonction
    path('Coach/<int:id>',details_coach,name="Hub_Coach_details"),
    path('listProjet',list_project,name="Hub_List_projet"),
    #path('listsecond', ProjectListView.as_view(),name="Hub_Project_List_Second"),
    #path('coachadd',Coach_add,name="Coach_add"),
    path('coachadd',Coach_addForm,name="Coach_add"),
    #path('coachadd3',Coach_addModelForm,name="Coach_add"),
    path('coachadd3',CoachCreateView.as_view(),name="Coach_add"),
    path('listStudent',ListStudent,name="Hub_Student_list"),
    path('Student/<int:id>',details_student,name="Hub_Student_details"),
]