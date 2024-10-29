from zebra import Zebra
import qrcode
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to generate EPL QR code command string
def generate_epl_qrcode(data):
    epl = f"""
N
q609
b50,100,Q,2,3,0,30,"{data}"
P1
    """
    return epl

# Function to send EPL to Zebra printer
def print_epl(epl_command):
    try:
        z = Zebra()
        z.setqueue("ZDesigner GC420t")  # Ensure this matches your system's printer name
        z.output(epl_command)
        logger.info("EPL command sent to printer successfully.")
    except Exception as e:
        logger.error(f"Error sending EPL to printer: {e}")

# Function to generate and save the QR code as an image
def generate_qrcode_image(data, filename="qrcode_image.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)

# Function to generate and print QR codes for a batch
def generate_qr_codes_batch(lot_number):
    serial_number = 1
    part_number = 1

    for i in range(lot_number):
        qr_data = f"SN: {serial_number}, PN: {part_number}, Lot: {lot_number}, Date: {datetime.datetime.now().date()}, Time: {datetime.datetime.now().time()}"
        epl_qrcode = generate_epl_qrcode(qr_data)
        print_epl(epl_qrcode)
        generate_qrcode_image(qr_data, f"qrcode_{serial_number}.png")
        serial_number += 1
        part_number += 1
        logger.info(f"Part {i + 1}/{lot_number} processed: SN {serial_number - 1}, PN {part_number - 1}")

    return f"QR codes for lot {lot_number} generated and printed successfully!"
