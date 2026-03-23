from django.shortcuts import render,redirect
from .forms import LoginForm
from .models import User

# Create your views here.

def loginPage(request):
    if request.method=="POST":
        form=request.POST #getting the input
        name=form.get("name") #input's name object
        password=form.get("password")
        user = User.objects.only("name","password","ID").filter(name=name).first() #getting name and password object from db
        if user.password==password: #if input's password equals to the password in db
            request.session["user_id"]=user.pk #cookie for isLogged security
            user.save()
            return redirect(f"/home/{user.name}") #redirect home
    return render(request,"accounts/login.html")

def register(request):
    form=LoginForm() #taking the forms
    if request.method=="POST":
        form=LoginForm(request.POST) #getting the input
        if form.is_valid():
            User.objects.create(
                name=form.cleaned_data["name"], #create a new row with input's values
                password=form.cleaned_data["password"]
            )
            user=User.objects.only("isOnline","pk").get(name=form.cleaned_data["name"])
            request.session["user_id"]=user.pk 
            user.isOnline=True 
            user.save()
            return redirect(f"/home/{form.cleaned_data["name"]}") #redirecting user's page
    return render(request,"accounts/register.html",{"form":form})

