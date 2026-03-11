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
            user=User.objects.only("name","password").get(name=name) #getting name and password object from db
            if user.password==form.cleaned_data["password"]: #if input's password equals to the password in db
                return redirect("/") #redirect home
    return render(request,"login.html",{"form":form})

