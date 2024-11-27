from django.urls import path
from polling_app import views
from dashboard import views


#Template Tagging
#app_name = 'polling_app'

urlpatterns = [
    
    path('index/', views.index, name="index"),
    #path('simple/', views.simple, name="simple"),
    path('vote/', views.vote, name="vote"),
    path('voter/', views.voter, name="voter"),
    path('candidate/', views.candidate, name="candidate"),
    path('position/', views.position, name="position"),
    
]