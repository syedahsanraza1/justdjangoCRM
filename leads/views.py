from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    #return HttpResponse("Hellow Worlld")
    return render(request, 'next_page.html')
