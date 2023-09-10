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
    return render(request, 'next_page.html' , context)
