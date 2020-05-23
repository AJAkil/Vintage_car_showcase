from django.urls import path
from . import views


urlpatterns = [
    path('allcars', views.show_all_cars, name='all_cars'),
    path('singlecar', views.show_single_car, name='single_car'),
    path('search', views.search, name='search')
]


