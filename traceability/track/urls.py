from django.urls import path
from .views import generate_and_display

urlpatterns = [
    path('', generate_and_display, name='home'),
]
