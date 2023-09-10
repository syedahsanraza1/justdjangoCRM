from django.shortcuts import render
from django.http import HttpResponse
from leads.models import Agent,leads

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