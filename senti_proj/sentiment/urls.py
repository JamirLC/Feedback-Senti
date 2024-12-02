from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.admin, name='admin'),
    path('generate/', views.generate, name='generate'),

    path('event/1/', views.event_1, name='event_1'),
    path('event/2/', views.event_2, name='event_2'),
    path('event/3/', views.event_3, name='event_3'),
    path('event/4/', views.event_4, name='event_4'),


]
