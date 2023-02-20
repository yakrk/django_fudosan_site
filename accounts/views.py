from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "User already exists")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect('register')
                else:
                    # create user
                    user = User.objects.create_user(
                        username= username,
                        password=password,
                        email = email,
                        first_name= first_name,
                        last_name = last_name
                    )
                    user.save()
                    messages.success(request, "You are now registered and can login")
                    return redirect ("login")
                    # login user
                    # auth.login(request, user)
                    # messages.success(request, "You are now logged in")
                    # return redirect('index')

        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:
        return render (request, "accounts/register.html")

def login(request):
    if request.method == "POST":
        username= request.POST["username"]
        password = request.POST["password"]
        
        user = auth.authenticate(username=username, password=password)
        
        # user exists?
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    else:
        return render (request, "accounts/login.html")

def logout(request):
    if request.method=="POST":
        auth.logout(request)
        messages.success(request, "You are not logged out")
        return redirect ("index")

def dashboard(request):
    if User.is_authenticated:
        contacts = Contact.objects.filter(user_id = request.user.id).order_by("-contact_date")
        context = {
            "contacts" : contacts   
        }
    return render (request, "accounts/dashboard.html", context)