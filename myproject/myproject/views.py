#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Hello Subham! I'm Learning Django. ")
    return render(request,'home.html')

def about(request):
    #return HttpResponse("I am Subham Rout. I am a student of Computer Science and Engineering. I am a beginner in Django.")
    return render(request,'about.html')