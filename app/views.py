from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required


UM = get_user_model()



def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        date_of_birth = request.POST.get("date_of_birth")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        if password == confirm_password:
            if UM.objects.filter(email=email).exists():
                messages.info(request, "Email already used once")
                return redirect("register")
            
            elif UM.objects.filter(username=username).exists():
                messages.info(request, "Username already used once")
                return redirect("register")
            
            elif not username:
                messages.info(request, "Username must be entered")
                return redirect("register")
            
            elif not email:
                messages.info(request, "Email must be entered")
                return redirect("register")
            
            elif not first_name:
                messages.info(request, "First Name must be entered")
                return redirect("register")
            
            elif not last_name:
                messages.info(request, "Last Name must be entered")
                return redirect("register")
            
            elif not date_of_birth:
                messages.info(request, "Birthday must be entered")
                return redirect("register")
            
            elif not password:
                messages.info(request, "Password must be entered")
                return redirect("register")
            
            elif not confirm_password:
                messages.info(request, "You must repeat the password for confirmation")
                return redirect("register")
                        
            else:
                user = UM.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, password=password)
                user.save()
                return redirect("login")
        
        else:
            messages.info(request, "Passwords don't match, please try again")
            return redirect("register")
    
    else:
        return render(request, "register.html")



def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            user_id = request.user.id
            return redirect(reverse("profile", args=[user_id]))
        
        else:
            messages.info(request, "Credentials Invalid")
            return redirect("login")
    
    else:
        return render(request, "login.html")


@login_required
def profile(request, pk):
    user_data = get_object_or_404(UM, id=pk)
    return render(request, "profile.html", {"user_data": user_data})


def logout(request):
    auth.logout(request)
    return redirect("register")
