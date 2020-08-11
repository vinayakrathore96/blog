from django.contrib import admin
from .models import UserProfile,InterviewPractice,Internship,Tips,ResumeTemplate,Job,FAQ,Guidance,Certification
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(InterviewPractice)
admin.site.register(Internship)
admin.site.register(Tips)
admin.site.register(ResumeTemplate)
admin.site.register(Job)
admin.site.register(FAQ)
admin.site.register(Guidance)
admin.site.register(Certification)