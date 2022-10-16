from django.urls import path

from codeforces import scrape
from . import views
urlpatterns = [
    path('hello/', views.sayhello),
    path('data/',scrape.All_User_data),
    
]