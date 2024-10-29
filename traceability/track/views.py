from django.shortcuts import render, HttpResponse
from .qr_utils import generate_qr_codes_batch
from .plc_utils import update_or_create_torque_data
import logging
from .models import TorqueData

logger = logging.getLogger(__name__)

# View to handle the form submission for QR codes
def generate_qr_codes(request):
    if request.method == "POST":
        try:
            lot_number = int(request.POST.get("lot_number"))  # Get the lot number from the form
            response_message = generate_qr_codes_batch(lot_number)
            return HttpResponse(response_message)
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            return HttpResponse(f"An error occurred: {e}")

    return render(request, 'track/index.html')

# View to handle PLC data fetching and updating database
def plc_data_view(request, part_number):
    response_message = update_or_create_torque_data(part_number)
    return HttpResponse(response_message)
    
def display_torque_data(request):
    torque_data_list = TorqueData.objects.all()  # Fetch all torque data records from the database
    return render(request, 'track/display_data.html', {'torque_data_list': torque_data_list})
