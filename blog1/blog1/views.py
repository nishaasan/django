from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>hello world!!</h1>")

def demo(request):
    return render(request,'index.html')