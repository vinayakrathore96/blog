from django.contrib.auth.password_validation import validate_password
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import RegistrationForm,ResumeUploadForm
from .models import FAQ,Guidance,Tips,InterviewPractice,ResumeTemplate,Internship,Job,Certification
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
import time

userbase = User
# Create your views here.
def login(request):
    if request.method == 'POST':
        userinput = request.POST['username']

        try:
            username = userbase.objects.get(email=userinput).username
        except userbase.DoesNotExist:
            username = request.POST['username']
        emp_password=request.POST['pswd']

        user=auth.authenticate(username = username,password = emp_password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid credentials')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)

    return redirect('home')


def home(request):
    return render(request,'homepage.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            userform = form.save(commit=False)
            if User.objects.filter(email=userform.email):
                messages.error(request,"Email already exists",extra_tags='success')
                return redirect('signup')
            userform.save()
            messages.info(request,'Account Created Successfully')
            return redirect('signup')
        else:
            messages.error(request,"Either Username already exists or Password's invalid",extra_tags='failed')
            return redirect('signup')

    else:
        form = RegistrationForm()

        args = {'form' : form}
        return render(request,'signin.html',args)


def skills(request):
    return render(request,'skills.html')

def important_tips(request):
    lists = Tips.objects.all()
    return render(request,'imp_tips.html', {'lists': lists})

def objectives(request):
    return render(request,'objective.html')

def goals(request):
    return render(request,'goals.html')

def requirements(request):
    return render(request,'requirements.html')

def jobs(request):
    lists = Job.objects.all()
    return render(request,'jobs.html',{'lists':lists})

def experiences(request):
    return render(request,'experiences.html')

def faqs(request):
    lists = FAQ.objects.all()
    return render(request,'faqs.html',{'lists':lists})

def guidance(request):
    lists = Guidance.objects.all()
    return render(request,'guidance.html',{'lists':lists})

def interview_practice(request):
    lists = InterviewPractice.objects.all()
    return render(request,'interview_ques.html',{'lists':lists})

def resume_template(request):
    lists = ResumeTemplate.objects.all()
    return render(request,'resume_templates.html',{'lists':lists})

def internship(request):
    lists = Internship.objects.all()
    return render(request,'internships.html',{'lists':lists})

def resume_upload(request):
    form = ResumeUploadForm(request.POST, instance = request.user)
    if form.is_valid():
        form.save()
        messages.info(request,"Resume Uploaded")
        return redirect('resume_upload')
    return render(request,'resume.html',{'form':form})


def hiring_process(request):
    return render(request, 'hiring_proc.html')

def certification(request):
    lists = Certification.objects.all()
    return render(request,'certification.html',{'lists':lists})