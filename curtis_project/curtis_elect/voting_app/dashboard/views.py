from django.shortcuts import render

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