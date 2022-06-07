from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from library.forms import LibraryForm
from library.models import Library

# Create your views here.
def register(request):                              #creating admin registration purpose
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():             #checking username already exists or not
                messages.info(request, 'Username is already taken')
                return redirect(register)
            elif User.objects.filter(email=email).exists():                 #checking email already exists or not
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                return redirect('login_user')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
            

    else:
        return render(request, 'registration.html')

def login_user(request):                                    #login purpose
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('show')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')



    else:
        return render(request, 'login.html')



def home(request):
    return render(request, 'home.html')


def logout_user(request):                               #logout purpose
    auth.logout(request)
    return redirect('home')

def show(request):                                      #reading book student view
    librarys = Library.objects.all()
    return render(request, "show.html", {'librarys': librarys})