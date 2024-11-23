from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def restaurant_page_Builder(request):
    return render(request,"restaurant_page_builder.html")

def signup_page(request):
    if request.method == 'POST':
        Username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        Email = request.POST['email']
        Password1 = request.POST['password1']
        Password2 = request.POST['password2']

        if Password1 == Password2:
            if User.objects.filter(username = Username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup_page')
            elif User.objects.filter(email = Email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup_page')
            else:
                user = User.objects.create_user(username=Username,first_name=firstname,last_name=lastname,email=Email,password=Password1)
                user.save()
                print('User Created')
        else:
            messages.info(request,'Password Not Matching...')
            return redirect('signup_page')
        return redirect('login_page')

    else:
        return render(request,'signup.html')
def login_page(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Password = request.POST['password']

        user = auth.authenticate(username = Username,password = Password)

        if user is not None:
            auth.login(request,user)
            return redirect('restaurant_page_Builder')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login_page')

    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

