from telnetlib import LOGOUT
from django.shortcuts import render, HttpResponseRedirect , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login, authenticate as auth_login, logout as auth_logout
from contactus.models import contactus
from blog.models import Post,Category
from django.contrib import messages


def index(request):
    posts = Post.objects.all()[:8]
    cat = Category.objects.all()[:8]
    data = {
        'posts':posts,
        'cat':cat
        }
    return render(request, "index.html",data)


def resume(request):
    return render(request, "resume.html")


def portfolio(request):
    return render(request, "portfolio.html")


def blog(request):
    #load all the post from db[10]
    posts = Post.objects.all()[:11]
    cat = Category.objects.all()
    data = {
        'posts':posts,
        'cat':cat
    }
    
    
    
    return render(request, "blog.html",data)


def contact(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        subject = request.POST['subject']
        desc = request.POST['desc']
        contact = contactus(fullname=fullname, email=email,
                            subject=subject, desc=desc)
        contact.save()
        messages.success(request, 'Your message has been successfully recorded ')


    return render(request, "contact.html")


def postcreation(request):

    return render(request, "postcreation.html")


def blogpost(request,url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    data = {
            'post':post,
            'cats':cats
        }
    
    return render(request, 'blogpost.html',data)


def category(request,url):
    cat = Category.objects.get(url=url)
    post = Post.objects.filter(cat=cat)
    data = {
        'cats':cat,       
        'post':post
    }
    return render(request, 'category.html',data)



def login_us(request):
    return render(request, "admin")
def register(request):
        if request.user.is_authenticated:
            return redirect('/')
        if request.method == "POST":
            
            # get the post paramaters
            regUsernameid = request.POST['regUsernameid']
            regFirstname = request.POST['regFirstname']
            regLastname = request.POST['regLastname']
            regPhoneno = request.POST['regPhoneno']
            regEmail = request.POST['regEmail']
            regPassword = request.POST['regPassword']
            regConfirmpassword = request.POST['regConfirmpassword']
            
            #check for  error
            if len(regUsernameid)>10:
                messages.error(request, 'Username must be under 10 characters')
                return redirect("register")
            elif regPassword != regConfirmpassword:
                messages.error(request, 'Password do not match')
                return redirect("register")



            else:
                myuser = User.objects.create_user(regUsernameid,regEmail,regPassword)
                myuser.first_name = regFirstname
                myuser.last_name = regLastname
                myuser.save() 
                messages.success(request, 'Your account has been successfully created ')
                return redirect("login_us")
    
        
        return render(request, "register.html")


def dashboard(request):
    
    return render(request, "dashboard.html")
  
    


def logout_us(request):
    auth_logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect("login_us")
    

