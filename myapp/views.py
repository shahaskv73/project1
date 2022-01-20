from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'home.html'),
    
def log(request):
        return render(request,'log.html'),

