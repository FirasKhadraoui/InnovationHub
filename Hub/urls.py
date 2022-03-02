import imp
from django.urls import path
from .views import HomePage, ListCoach, details_coach, list_project


urlpatterns=[
    path('home',HomePage,name="Hub_home"),
    path('listCoach',ListCoach,name="Hub_Coach_list"),
    #path('Coach',details_coach,name="Hub_Coach_details"), #id statique dans la fonction
    path('Coach/<int:id>',details_coach,name="Hub_Coach_details"),
    path('listProjet',list_project,name="Hub_List_projet"),
]