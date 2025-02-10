from zebra import Zebra
import qrcode
import datetime
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the output directory for QR codes
OUTPUT_DIR = r"D:\Shubham\Fourfront\Traceability_python\traceability\qrcodes"

# Function to generate ZPL QR code command string
def generate_zpl_qrcode(data):
    zpl = f"""
    CT~~CD,~CC^~CT~
    ^XA~TA000~JSN^LT0^MNW^MTT^PON^PMN^LH0,0^JMA^PR2,2~SD15^JUS^LRN^CI0^XZ
    ^XA
    ^MMT
    ^PW400
    ^LL0200
    ^LS0
    ^FT119,200^BQN,2,4
    ^FH\\^FDLA,{data}^FS
    ^PQ1,0,1,Y^XZ
    """
    return zpl

# Function to send ZPL to Zebra printer
def print_zpl(zpl_command):
    try:
        z = Zebra()
        z.setqueue("ZDesigner GC420t (copy 1)")  # Update with your printer name
        z.output(zpl_command)
        logger.info("ZPL command sent to printer successfully.")
    except Exception as e:
        logger.error(f"Error sending ZPL to printer: {e}")

# Function to generate and save a single QR code image
def generate_qrcode_image(data, filename="qrcode_image.png"):
    os.makedirs(OUTPUT_DIR, exist_ok=True)  # Ensure the output directory exists
    filepath = os.path.join(OUTPUT_DIR, filename)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(filepath)
    logger.info(f"QR code saved at {filepath}")

# Function to print only **one** QR code per click
def generate_qr_codes_batch(lot_number, serial_number):
    """ Generates and prints only ONE QR code per function call """
    # Get current date and time
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Create QR code data
    qr_data = (
        f"SN: {serial_number}\n"
        f"PN: {serial_number}\n"  # Use serial number as part number
        f"Lot: {lot_number}\n"
        f"Date: {current_date}\n"
        f"Time: {current_time}"
    )

    # Generate and send to printer
    zpl_qrcode = generate_zpl_qrcode(qr_data)
    print_zpl(zpl_qrcode)

    # Generate and save QR code image
    generate_qrcode_image(qr_data, f"qrcode_{serial_number}.png")

    logger.info(f"Printed: SN {serial_number}, Lot {lot_number}")

    return f"QR code for SN {serial_number} in Lot {lot_number} printed successfully!"
