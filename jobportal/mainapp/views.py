from django.shortcuts import render,HttpResponse,redirect , get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from . models import *

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

def logout_user(request):
    logout(request)
    return redirect('/')

from .forms import RegistrationForm
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form':form})

def index(request):
    jobs = jobpost.objects.all()[:4]
    test = testimonials.objects.all()
    return render(request, 'index.html',{'jobs':jobs, 'test':test})

def userProfile(request):
    return render(request, 'userProfile.html', {})

from django.views.generic import ListView
class jobs(ListView):
    template_name = 'browse-job.html'
    model = jobpost
    context_object_name = 'jobposts'

class my_jobs(ListView):
    template_name = 'browse-my-job.html'
    model = jobpost
    context_object_name = 'post'

# def jobs(request):
#     return render(request, 'browse-job.html')


    

from . forms import jobpostForm
def createjob(request):
    if request.method == "POST":
        form = jobpostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.job_provider = request.user
            data.save()
            form.save_m2m()
            return redirect('my_jobs')
    else:
        form = jobpostForm()
    return render(request, 'jobposting.html', {'form':form})


from . forms import jobpostFormForFree
def createjobasfreelancher(request):
    if request.method == "POST":
        form = jobpostFormForFree(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.job_provider = request.user
            data.save()
            form.save_m2m()
            return redirect('my_jobs')
    else:
        form = jobpostFormForFree()
    return render(request, 'jobpostingforfree.html', {'form':form})

def jobdetail(request, id=id):
    post = get_object_or_404(jobpost,id=id)
    # post = None
    return render(request, 'jobdetail.html', {'post':post})

# from . forms import jobpostForm
def apply_done(request):
    # form = jobpostForm()
    # form.Candidates = request.user
    # form.save()
    return render(request, 'apply_done.html')

from . forms import my_profileForm
def editProfile(request):
    if request.method == "POST":
        form = my_profileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userProfile/')
    else:
        form = my_profileForm()
    return render(request, 'edit_profile.html', {'form':form})

    

def freelancer(request):
    free_jobs = freelancer_job.objects.all()
    return render(request, 'browse-candidates.html', {'free_jobs':free_jobs})

def freelancher_detail(request,  id=id):
    post = get_object_or_404(freelancer_job,id=id)
    # post = None
    return render(request, 'jobpostingforfree_details.html', {'post':post})

def blog_index(request):
    return render(request, 'blog-classic-sidebar.html')

def blog_details(request):

    return render(request, 'blog-details.html')

def portfolio_grid(request):
    return render(request, 'portfolio-grid-3.html')

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    info = Website_Details.objects.get(id=1)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # print(name, email, message)
        obj = ContactUs(name = name, email = email, message = message)
        obj.save()
    return render(request, 'contact.html', {'site_info':info})