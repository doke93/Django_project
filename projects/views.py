from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def projects(requets):
    return render(requets, 'projects.html')

def project(requets, pk):
    return HttpResponse('Single project' +' '+str(pk))