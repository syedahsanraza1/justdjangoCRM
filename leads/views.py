from django.shortcuts import render
from django.http import HttpResponse
from leads.models import Agent,leads
from .forms import leadform

# Create your views here.

def home_page(request):
    #return HttpResponse("Hellow Worlld")
    lead = leads.objects.all()
    context ={
        "leads" : lead
    }
    return render(request, 'leads/home_page.html' , context)

def lead_detail(request,pk):
    lead_detail_view = leads.objects.get(id=pk)
    context = {
        "lead_detail_view1" : lead_detail_view
    }
    return render(request , 'leads/leads_details.html' , context)

def create_leads(request):
    print(request.POST)
    if request.method =="POST":
        print("Reciving post request")
        form = leadform(request.POST)
        if form.is_valid():
            print("checking if data is valid")
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
    context = {
        "form" : leadform()
    }
    return render(request , 'leads/create_leads.html',context)

