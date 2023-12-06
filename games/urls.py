from django.urls import path
from games.views import sobre

urlpatterns = [
    path('sobre/', sobre),
    
]

