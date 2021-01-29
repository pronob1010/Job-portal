from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('jobs/', views.jobs, name="jobs"),
    path('login/', views.login_user, name="login"),
    path('register/', views.register, name="register"),
    path('freelancer/', views.freelancer, name="freelancer"),
    path('jobdetail/', views.jobdetail, name="jobdetail"),
    path('blog/', views.blog_index, name="blog"),
    path('blog_details/', views.blog_details, name="blog_details"),
    path('portfolio_grid/', views.portfolio_grid, name="portfolio_grid"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]
