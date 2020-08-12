"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('skills/',views.skills,name='skills'),
    path('important_tips/',views.important_tips,name='important_tips'),
    path('objectives/',views.objectives,name='objectives'),
    path('goals/',views.goals,name='goals'),
    path('requirements/',views.requirements,name='requirements'),
    path('jobs/',views.jobs,name='jobs'),
    path('experiences/',views.experiences,name='experiences'),
    path('faqs/',views.faqs,name='faqs'),
    path('interview_practice/',views.interview_practice,name='interview_practice'),
    path('resume_template/', views.resume_template, name='resume_template'),
    path('internship/', views.internship, name='internship'),
    path('guidance/', views.guidance, name='guidance'),
    path('resume_upload/', views.resume_upload, name='resume_upload'),
    path('logout/',views.logout,name='logout'),
    path('hiring_process/', views.hiring_process, name='hiring_process'),
    path('certification/', views.certification, name='certification')
]
