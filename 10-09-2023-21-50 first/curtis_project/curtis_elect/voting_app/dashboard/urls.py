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
    path('candidate_add/', views.candidate_add, name="candidate_add"),
    path('candidate_edit/', views.candidate_edit, name="candidate_edit"),
    path('voter_add/', views.voter_add, name="voter_add"),
    path('voter_edit/<int:id>', views.voter_edit, name="voter_edit"),
    
    
]