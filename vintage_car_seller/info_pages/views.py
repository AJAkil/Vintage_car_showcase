from django.shortcuts import render

def index(request):
    return render(request,'info_pages/index.html')

def about_us(request):
    return render(request, 'info_pages/about.html')