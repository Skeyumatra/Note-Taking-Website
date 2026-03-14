from django.shortcuts import render,redirect
from . import models

# Create your views here.
def entry(request):
    return redirect("/accounts/login") #because of this, they encounter with login when the user enter the main domain


def homePage(request,name):
    user=models.User.objects.get(name=name) #getting user's objects
    notes=user.notes.all() #getting the user's child table Note
    if user.isOnline==True: #if user log in
        data={"user":user,"notes":notes} #required informations
        return render(request,"base/home.html",data) #rendering home/user/ page
    else:
        return redirect("/") #if users doesnt log in don't allow them to enter the page home/user/ page
    
def note(request,name,pk):
    username=models.User.objects.only("name").get(name=name)
    note=models.Note.objects.get(user__name=name,pk=pk) #getting the desired note of user
    return render(request,"base/note.html",{"note":note,"name":username.name})

def addNote(request,name):
    if request.method=="POST":
        form=request.POST #getting form
        user=models.User.objects.get(name=name) #getting user for foreingkey object
        models.Note.objects.create(  #creating new note object
            user=user,
            title=form.get("title"),
            content=form.get("content")
        )
        return redirect(f"/home/{name}")
    return render(request,"base/addNote.html")

def updateNote(request,name,pk):
    if request.method=="POST":
        form=request.POST
        note=models.Note.objects.get(user__name=name,pk=pk)
        note.title=form.get("title")
        note.content=form.get("content")
        note.save()
        return redirect(f"/home/{name}")
    return render(request,"base/updateNote.html")
    
def deleteNote(request,name,pk):
    note=models.Note.objects.get(user__name=name, pk=pk) #getting the required note
    note.delete() #delete
    return redirect(f"/home/{name}") #redirecting user main page

def exit(request,name):
    exit=models.User.objects.only("isOnline").get(name=name) #getting the user activity information for that moment
    exit.isOnline=False 
    exit.save() #user is offline now so he/she logged out
    return redirect("/")
            