from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='vr-landing'), 
    #'' empty string, initial page
    path('about/', views.about, name='vr-about'),
]
