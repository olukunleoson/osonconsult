from django.shortcuts import render

# Create your views here.
def program(request):
    return render(request, 'programs/programs.html')

def iskilld(request):
    return render(request, 'programs/iskilld.html')

def cyt(request):
    return render(request, 'programs/cyt.html')

def Nations_league(request):
    return render(request, 'programs/Nleague.html')