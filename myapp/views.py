from django import views
from django.shortcuts import render
from django.views import View
from .forms import ResumeForm
from .models import Resume

class HomeView(View):
    def get(self,request):
        form=ResumeForm()
        candidates=Resume.objects.all()
        return render(request,'myapp/home.html',{'candidates':candidates,'form':form})
    def post(self,request):
        form=ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return render(request,'myapp/home.html',{'form':form})

class CandidateView(View):
    def get(self,request,pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'myapp/candidate.html', {'candidate':candidate})
        