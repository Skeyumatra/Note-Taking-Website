from django.shortcuts import render,redirect
from . import models

# Create your views here.
def entry(request):
    return redirect("/accounts/login") #because of this, they encounter with login when the user enter the main domain


def homePage(request,name):
    user=models.models.User.objects.get(name=name) #getting user's objects
    if user.isOnline==True: #if user log in
        data={"user":user} #user informations
        return render(request,"home.html",data) #rendering home/user/ page
    else:
        return redirect("/") #if users doesnt log in don't allow them to enter the page home/user/ page
    

def exit(request,name):
    exit=models.models.User.objects.only("isOnline").get(name=name) #getting the user activity information for that moment
    exit.isOnline=False 
    exit.save() #user is offline now so he/she logged out
    return redirect("/")
            