import imp
from django.urls import path
from .views import Coach_add, Coach_addForm, HomePage, ListCoach, details_coach, list_project


urlpatterns=[
    path('home',HomePage,name="Hub_home"),
    path('listCoach',ListCoach,name="Hub_Coach_list"),
    #path('Coach',details_coach,name="Hub_Coach_details"), #id statique dans la fonction
    path('Coach/<int:id>',details_coach,name="Hub_Coach_details"),
    path('listProjet',list_project,name="Hub_List_projet"),
    #path('listsecond', ProjectListView.as_view(),name="Hub_Project_List_Second"),
    #path('coachadd',Coach_add,name="Coach_add"),
    path('coachadd',Coach_addForm,name="Coach_add"),
]