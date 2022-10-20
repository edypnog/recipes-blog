from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')

def contact(request):
    return HttpResponse('home')

def about(request):
    return HttpResponse('home')

