from django.shortcuts import render, HttpResponse
from .qr_utils import generate_qr_codes_batch
from .models import TorqueData
import logging

logger = logging.getLogger(__name__)

# Combined view
def generate_and_display(request):
    message = None
    if request.method == "POST":
        try:
            lot_number = int(request.POST.get("lot_number"))  # Get the lot number from the form
            message = generate_qr_codes_batch(lot_number)  # Generate QR codes
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            message = f"An error occurred: {e}"

    # Fetch all torque data
    torque_data_list = TorqueData.objects.all()
    return render(request, 'track/combined_page.html', {
        'torque_data_list': torque_data_list,
        'message': message
    })
