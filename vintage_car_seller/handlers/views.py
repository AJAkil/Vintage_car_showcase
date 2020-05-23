from django.shortcuts import render

def show_all_handlers(request):
    return render(request, 'handlers/all_handlers.html')

def show_single_handler(request):
    return render(request, 'handlers/single_handler.html')