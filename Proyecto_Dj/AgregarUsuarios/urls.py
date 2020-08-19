from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('wordcloud', views.dashboard1),
    path('alcance', views.dashboard2),
    path('logout', views.logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')), 

] 