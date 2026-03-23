from django.shortcuts import render,redirect
from . import models

# Create your views here.
def entry(request):
    try:    
        session=request.session["user_id"] #getting the cookie
        user=models.User.objects.only("name").get(pk=session) #if User id equals to session ID, that means that the account was logged in before in the browser
        return redirect(f"/home/{user.name}")  
    except:
        return redirect("/accounts/login") #because of this, they encounter with login when the user enter the main domain if user didn't login before


def homePage(request,name):
    try:
        session=request.session["user_id"]
        user=models.User.objects.only("name").get(name=name,pk=session) #getting user's objects
        notes=user.notes.all() #getting the user's child table Note
        data={"user":user,"notes":notes} #required informations
        return render(request,"base/home.html",data) #rendering home/user/ page
    except:
        return redirect("/")
    
def note(request,name,pk):
    try:
        session=request.session["user_id"] #getting the cookie
        username=models.User.objects.only("name","isOnline").get(name=name,pk=session) 
        note=models.Note.objects.get(user__name=name,pk=pk) #getting the desired note of user
        return render(request,"base/note.html",{"note":note,"name":username.name})
    except:
        return redirect("/")

def addNote(request,name):
    try:
        session=request.session["user_id"] #getting the cookie
        user=models.User.objects.get(name=name,pk=session) #getting user for foreingkey object
        if request.method=="POST":
            form=request.POST #getting form
            models.Note.objects.create(  #creating new note object
                user=user,
                title=form.get("title"),
                content=form.get("content")
            )
            return redirect(f"/home/{name}")
        return render(request,"base/addNote.html")
    except:
        return redirect("/")
            

def updateNote(request,name,pk):
    try:
        session=request.session["user_id"] #getting the cookie
        note=models.Note.objects.get(user__pk=session,pk=pk)
        if request.method=="POST":
            form=request.POST
            note.title=form.get("title")
            note.content=form.get("content")
            note.save()
            return redirect(f"/home/{name}")
        return render(request,"base/updateNote.html")
    except:
        return redirect("/")
    
def deleteNote(request,name,pk):
    try:
        session=request.session["user_id"] #getting the cookie
        note=models.Note.objects.get(user__pk=session, pk=pk) #getting the required note
        note.delete() #delete
        return redirect(f"/home/{name}") #redirecting user main page
    except:
        return redirect("/")

def exit(request,name):
    try:  
        session=request.session["user_id"] #getting the cookie
        exit=models.User.objects.only("isOnline").get(name=name,pk=session) #getting the user activity information for that moment
        exit.isOnline=False 
        exit.save() #user is offline now so he/she logged out
        request.session.flush() #deleting the session_id cookie
        return redirect("/")
    except:
        return redirect("/")        