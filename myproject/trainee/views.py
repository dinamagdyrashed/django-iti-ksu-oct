from django.shortcuts import render
from django.http import HttpResponse
from .models import Trainee
# Create your views here.
def alltrainee(request):
    # trainee=[[1,'Ahmed','ahmed@email.com','photo'],[2,'Mohamed','mo@email.com','photo']]
    trainee=Trainee.objects.all()
    return render(request,'alltrainee.html',context={'trainee':trainee})

def gettraineeid(request):
    return HttpResponse("<h1>welcome to this trainee</h1>")

def inserttrainee(request):
    print(request.POST)
    if request.method=='POST':
        name=request.POST['trname']
        email=request.POST['tremail']
        img=request.FILES['trphoto']
        Trainee.objects.create(name=name,email=email,photo=img)
        print(name,email,img)
    return render(request,'insert.html')
def updatetrainee(request,id):
    return HttpResponse(f"<h1>welcome to update trainee {id}</h1>")

def deletetrainee(request,id):
    return HttpResponse(f"<h1>welcome to delete trainee {id}</h1>")