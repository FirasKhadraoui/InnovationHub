import imp
from django.urls import path
from .views import HomePage, ListCoach


urlpatterns=[
    path('home',HomePage,name="Hub_home"),
    path('listCoach',ListCoach,name="Hub_Coach_list"),
]