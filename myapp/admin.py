from django import forms
from django.contrib import admin
from django.forms import widgets


from .models import Resume



@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'DOB', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'job_city', 'profile_img', 'my_document']


