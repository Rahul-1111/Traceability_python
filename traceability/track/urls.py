from django.urls import path
from .views import generate_qr_codes, plc_data_view, display_torque_data

urlpatterns = [
    path('', generate_qr_codes, name='home'),
    path('generate_qr_codes/', generate_qr_codes, name='generate_qr_codes'),
    path('plc-data/', plc_data_view, name='plc-data'),
    path('display_data/', display_torque_data, name='display_data'),  # Add this line
]
