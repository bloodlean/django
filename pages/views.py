from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def sale(request):
    return render(request, 'pages/sale.html')

def repairs(request):
    return render(request, 'pages/repairs.html')

