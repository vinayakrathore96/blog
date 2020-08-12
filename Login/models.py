from django.db import models
from django.contrib.auth.models import User
# Create your models here.


COUNTRY_CHOICES = (
    ("India", "India"),
    ("United States Of America", "U.S.A"),
    ("United Kingdom", "U.K"),
    ("Australia", "Australia"),
    ("China", "China"),
    ("Japan", "Japan"),
    ("Canada", "Canada"),
    ("Africa", "Africa"),
)



class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    address = models.TextField(max_length=250,blank=True,null=True)
    resume = models.FileField(blank=True,null=True)
    def __str__(self):
        return self.user.username

#class Resume(models.Model):




class InterviewPractice(models.Model):
    question = models.TextField(max_length=250,blank=True,null=True)
    answer = models.TextField(max_length=1000,blank=True,null=True)
    def __str__(self):
        return self.question

class Internship(models.Model):
    reference_Id = models.CharField(max_length=100,primary_key=True,default='1')
    position = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(max_length=400,blank=True,null=True)
    def __str__(self):
        return self.position

class ResumeTemplate(models.Model):
    resumetemplate = models.ImageField(upload_to='Resume_Template',blank=True,null=True)

class FAQ(models.Model):
    question = models.TextField(max_length=250, blank=True, null=True)
    answer = models.TextField(max_length=1000, blank=True, null=True)
    def __str__(self):
        return self.question

class Job(models.Model):
    reference_Id = models.CharField(max_length=100, primary_key=True, default='1')
    position = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=400, blank=True, null=True)
    experience = models.TextField(max_length=300, blank=True, null=True)
    def __str__(self):
        return self.position

class Guidance(models.Model):
    content = models.TextField(max_length=260,blank=True,null=True)

class Tips(models.Model):
    tip = models.TextField(max_length=260,blank=True,null=True)
    def __str__(self):
        return self.tip


class Certification(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    organiser = models.CharField(max_length=150,blank=True,null=True)
