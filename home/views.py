from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
from .import views

def home(request):
    person = Person.objects.all()
    context = {'person':person}
    return render(request,'index.html',context)

def add(request,id=0):
    if request.method == 'GET':
        if id == 0:

            form = PersonForm()
        else:
            person = Person.objects.get(pk=id)
            form = PersonForm(instance = person)
        context = {'form':form}
        return render(request,'add.html',context)


    else:
        if id == 0:
            form = PersonForm(request.POST)
        else:
            person = Person.objects.get(pk=id)
            form = PersonForm(request.POST,instance = person)

        if form.is_valid():
            form.save()
        return redirect('/add')
 
 
 
def delete(request,id):
    person = Person.objects.get(pk=id)
    person.delete()
    return redirect("/")

