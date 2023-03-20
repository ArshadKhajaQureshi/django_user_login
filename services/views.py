from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
#the user and auth we import here helps us to getmodels through which we save data in Database

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, "login.html")


def register(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        email=request.POST["email"]
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("username taken") #it will be printed in console
                
                # importing messages from contrib (above in imports) and using here to print message in the browser and not in console 
            #checking whether in database we have same username from the User class we imported
            elif User.objects.filter(email=email).exists():
                print("email already taken")
            else:    
                user=User.objects.create_user(first_name=first_name,username=username,password=password1,email=email,last_name=last_name)
                #here all the variables are available in database like first_name  etc
                user.save();
                print("user created")
                return redirect("login")
        else:
            print("password not matching")
        return redirect('/')#if not given cannot render the html ( Value error comes)
    else:    
        # to handle database we use USer.objects and for creating user we use command create_user
        print("form calling")
        return render(request, 'register.html')
        #when u call the register page the else part gets executed and u see the page of registration in browser
        #when u submit the POST method is called andfrom django.shortcuts import render

def logout(request):
    auth.logout(request)
    return redirect('/')



