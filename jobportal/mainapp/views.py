from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


def index(request):
    return render(request, 'index.html')

def jobs(request):
    return render(request, 'browse-job.html')

def freelancer(request):
    return render(request, 'browse-candidates.html')

def job_detail(request):
    return render(request, 'job-detail.html')

def blog_index(request):
    return render(request, 'blog-classic-sidebar.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def portfolio_grid(request):
    return render(request, 'portfolio-grid-3.html')

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')