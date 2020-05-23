from django.shortcuts import render

# Create your views here.
def show_all_cars(request):
    return render(request, 'cars/all_cars.html')

def show_single_car(request):
    return render(request, 'cars/single_car.html')

def search(request):
    return render(request, 'cars/search.html')