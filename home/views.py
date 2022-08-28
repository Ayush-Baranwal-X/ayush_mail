from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from home.models import Info
from home.models import Feedback
from home.models import Mail
import datetime

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    user_name = request.user.username
    context = {
        'home_tab' : 'active',
        'user_name' : user_name,
    }
    return render(request, 'index.html', context)

def mails(request):
    if request.user.is_anonymous:
        return redirect('/login')
    mails = Mail.objects.filter(touser=request.user.username).order_by('date')
    number = mails.count()
    context = {
        'mails_tab' : 'active',
        'mails' : mails,
        'number' : number,
        'user_name' : request.user.username,
    }
    return render(request, 'mails.html', context)

def mail(request,pk):
    if request.user.is_anonymous:
        return redirect('/login')
    # mails = Mail.objects.get(pk = pk)
    mail = get_object_or_404(Mail,pk = pk)
    context = {
        'mails_tab' : 'active',
        'mail' : mail,
        'user_name' : request.user.username,
    }
    return render(request, 'mail.html', context)

def delete(request,pk):
    if request.user.is_anonymous:
        return redirect('/login')
    # mails = Mail.objects.get(pk = pk)
    mail = get_object_or_404(Mail,pk = pk)
    mail.delete()
    return redirect('/mails')

def about(request):
    if request.user.is_anonymous:
        return redirect('/login')
    context = {
        'user_name' : request.user.username,
    }
    return render(request, 'about.html', context)

def contact(request):
    if request.user.is_anonymous:
        return redirect('/login')
    context = {
        'contact_tab' : 'active',
        'user_name' : request.user.username,
    }
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")
        date = datetime.datetime.now()
        if name == "" or email == "" or phone == "" or comment == "":
            messages.warning(request, 'You are required to fill all feilds!')
            return render(request, 'contact.html', context)
        else:
            feedback = Feedback(name = name , email = email, phone = phone, comment = comment, date = date)
            feedback.save()
            messages.success(request, 'Feedback submitted successfully!')
            return redirect('/')
    return render(request, 'contact.html', context)

def sendmail(request):
    if request.user.is_anonymous:
        return redirect('/login')
    contacts = User.objects.all()
    context = {
        'sendmail_tab' : 'active',
        'contacts': contacts,
        'user_name' : request.user.username,
    }
    if request.method == "POST":
        fromuser = request.user.username
        touser = request.POST.get("touser")
        subject = request.POST.get("subject")
        body = request.POST.get("body")
        date = datetime.datetime.now()
        if fromuser == "" or touser == "" or subject == "" or body == "":
            messages.warning(request, 'You are required to fill all feilds!')
            return render(request, 'sendmail.html', context)
        else:
            if User.objects.filter(username=touser).exists():
                mail = Mail(fromuser=fromuser,touser=touser,subject=subject,body=body,date=date)
                mail.save()
                messages.success(request, 'Mail sent successfully!')
                return redirect('/')
            else:
                messages.warning(request, 'Invalid Username entered in the To feild!')
                return redirect('/sendmail')
    return render(request, 'sendmail.html', context)

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Log in Successful!')
            return redirect('/')
            # A backend authenticated the credentials
        else:
            messages.warning(request, 'Wrong Username or Password!')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        country = request.POST.get("country")
        gender = request.POST.get("gender")
        date = datetime.datetime.now()
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.warning(request, 'Your account already exists. Try logging in!')
            return redirect('/login')
        else:
            if username == "" or password == "" or name == "" or email == "" or phone == "" or country == "":
                messages.warning(request, 'You are required to fill all feilds!')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username,email,password,first_name = name)
                user.save()
                info = Info(name=name,email=email,username=username,gender=gender,phone=phone,country=country,date=date)
                info.save()
                messages.success(request, 'Account Created Successful!')
                return redirect('/login')
    return render(request, 'signup.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('/login')