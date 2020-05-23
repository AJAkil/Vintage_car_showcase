from django.urls import path
from . import views


urlpatterns = [
    path('allhandlers', views.show_all_handlers, name='all_handlers'),
    path('handler', views.show_single_handler, name='single_handler'),
]


