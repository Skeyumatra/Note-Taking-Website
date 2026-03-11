from django.shortcuts import render,redirect
from .forms import LoginForm
from .models import User

# Create your views here.

def loginPage(request):
    form=LoginForm()  #taking forms for name and password object
    if request.method=="POST":
        form=LoginForm(request.POST) #getting the input
        if form.is_valid():
            name=form.cleaned_data["name"] #input's name object
            user=User.objects.only("name","password","isOnline").get(name=name) #getting name and password object from db
            if user.password==form.cleaned_data["password"]: #if input's password equals to the password in db
                user.isOnline=True
                user.save()
                return redirect(f"/home/{user.name}") #redirect home
    return render(request,"login.html",{"form":form})

def register(request):
    form=LoginForm() #taking the forms
    if request.method=="POST":
        form=LoginForm(request.POST) #getting the input
        if form.is_valid():
            User.objects.create(
                name=form.cleaned_data["name"], #create a new row with input's values
                password=form.cleaned_data["password"]
            )
            online=User.objects.only("isOnline").get(name=form.cleaned_data["name"])
            online.isOnline=True #automatically log in
            online.save()
            return redirect(f"/home/{form.cleaned_data["name"]}") #redirecting user's page
    return render(request,"register.html",{"form":form})

