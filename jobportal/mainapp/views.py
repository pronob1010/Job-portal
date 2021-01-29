from django.shortcuts import render,HttpResponse,redirect
from mainapp.models import ContactUs
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request =request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Username and password')
        else:
            messages.error(request, 'Invalid Username and password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form}) 


def register(request):
    return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')

def jobs(request):
    return render(request, 'browse-job.html')

def freelancer(request):
    return render(request, 'browse-candidates.html')

def jobdetail(request):
    return render(request, 'jobdetail.html')

def blog_index(request):
    return render(request, 'blog-classic-sidebar.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def portfolio_grid(request):
    return render(request, 'portfolio-grid-3.html')

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # print(name, email, message)
        obj = ContactUs(name = name, email = email, message = message)
        obj.save()
    return render(request, 'contact.html')