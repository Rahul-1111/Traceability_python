from django.shortcuts import render
from django.http import JsonResponse
from .qr_utils import generate_qr_codes_batch
from .models import TorqueData
import logging
from django.contrib import admin

admin.site.index_title = 'Tracebility'
admin.site.site_header = 'Admin'
admin.site.site_title = 'Tracebility'

logger = logging.getLogger(__name__)

# View for rendering the combined page
def combined_page(request):
    return render(request, 'track/combined_page.html')

# View to handle QR code generation
def generate_qr_codes(request):
    if request.method == "POST":
        try:
            lot_number = int(request.POST.get("lot_number"))  # Get the lot number from the form
            response_message = generate_qr_codes_batch(lot_number)
            return JsonResponse({"message": response_message})
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            return JsonResponse({"error": str(e)}, status=400)

# API endpoint to fetch torque data as JSON
def fetch_torque_data(request):
    if request.method == "GET":
        data = list(TorqueData.objects.values())  # Fetch all data as a list of dictionaries
        return JsonResponse({"data": data})
