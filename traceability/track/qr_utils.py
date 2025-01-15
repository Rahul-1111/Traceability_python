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
^FH\^FDLA,{data}^FS
^PQ1,0,1,Y^XZ
    """
    return zpl

# Function to send ZPL to Zebra printer
def print_zpl(zpl_command):
    try:
        z = Zebra()
        z.setqueue("ZDesigner GC420t (copy 1)")  # Ensure this matches your system's printer name
        z.output(zpl_command)
        logger.info("ZPL command sent to printer successfully.")
    except Exception as e:
        logger.error(f"Error sending ZPL to printer: {e}")

# Function to generate and save the QR code as an image
def generate_qrcode_image(data, filename="qrcode_image.png"):
    # Ensure the output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Create the full path to save the image
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

# Function to generate and print QR codes for a batch
def generate_qr_codes_batch(lot_number):
    serial_number = 1
    part_number = 1

    for i in range(lot_number):
        qr_data = f"SN: {serial_number}, PN: {part_number}, Lot: {lot_number}, Date: {datetime.datetime.now().date()}, Time: {datetime.datetime.now().time()}"
        
        # Generate ZPL QR code command
        zpl_qrcode = generate_zpl_qrcode(qr_data)
        
        # Print the ZPL command to the Zebra printer
        print_zpl(zpl_qrcode)
        
        # Generate and save the QR code image
        generate_qrcode_image(qr_data, f"qrcode_{serial_number}.png")
        
        serial_number += 1
        part_number += 1
        logger.info(f"Part {i + 1}/{lot_number} processed: SN {serial_number - 1}, PN {part_number - 1}")

    return f"QR codes for lot {lot_number} generated and printed successfully!"
