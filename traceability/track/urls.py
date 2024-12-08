from django.urls import path
from .views import combined_page, generate_qr_codes, fetch_torque_data

urlpatterns = [
    path('', combined_page, name='combined_page'),
    path('generate_qr_codes/', generate_qr_codes, name='generate_qr_codes'),
    path('fetch_torque_data/', fetch_torque_data, name='fetch_torque_data'),
]
