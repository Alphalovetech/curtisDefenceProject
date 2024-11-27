from django.shortcuts import render
from polling_app.models import *

# Create your views here.

def index(request):
    return render(request, 'adminlte/index.html', {})

# def simple(request):
#     return render(request, 'adminlte/pages/tables/simple.html', {})

def vote(request):
    return render(request, 'adminlte/pages/voting_info/vote.html', {})

def voter(request):
    return render(request, 'adminlte/pages/voting_info/voter.html')

def candidate(request):
    return render(request, 'adminlte/pages/candidate_info/candidate.html')

def position(request):
    return render(request, 'adminlte/pages/candidate_info/position.html')

def candidate_add(request):
    return render(request, 'adminlte/pages/candidate_info/candidate_add.html')

def candidate_edit(request):
    return render(request, 'adminlte/pages/candidate_info/candidate_edit.html')

def voter_add(request):
    return render(request, 'adminlte/pages/voting_info/voter_add.html')

def voter_edit(request):
    return render(request, 'adminlte/pages/voting_info/voter_edit.html')