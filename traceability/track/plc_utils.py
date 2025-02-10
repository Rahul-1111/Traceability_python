from datetime import datetime, time
import logging
from pymodbus3.client import ModbusTcpClient
from .models import TorqueData
import qrcode


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the get_current_shift function
def get_current_shift() -> str:
    now = datetime.now().time()
    if time(7, 0) <= now < time(15, 30):
        return 'Shift 1'
    elif time(15, 30) <= now < time(23, 59):
        return 'Shift 2'
    else:
        return 'Shift 3'

# Function to fetch PLC data
def fetch_plc_data():
    client = ModbusTcpClient('192.168.0.1', port=502)
    if not client.connect():
        logger.error("Unable to connect to Modbus server.")
        return {}

    # Assuming torque data is stored in holding registers
    try:
        torque_data = {
            "station1": client.read_holding_registers(0, 3),
            "station2": client.read_holding_registers(3, 3),
            "station3": client.read_holding_registers(6, 3),
            "station4": client.read_holding_registers(9, 3),
        }
    except Exception as e:
        logger.error(f"Error reading from Modbus server: {e}")
        return {}
    finally:
        client.close()
    
    return torque_data

# Function to update or create TorqueData entry
def update_or_create_torque_data(part_number):
    shift = get_current_shift()  # Automatically determine the shift
    torque_data = fetch_plc_data()

    # Check for errors in data fetching
    if not torque_data or any(data.isError() for data in torque_data.values()):
        return "Error fetching PLC data."

    # Extracting data from the fetched values
    station_data = {
        "station1_torque1": torque_data['station1'].registers[0],
        "station1_torque2": torque_data['station1'].registers[1],
        "station1_torque3": torque_data['station1'].registers[2],
        "station1_status": "OK",

        "station2_torque1": torque_data['station2'].registers[0],
        "station2_torque2": torque_data['station2'].registers[1],
        "station2_torque3": torque_data['station2'].registers[2],
        "station2_status": "OK",

        "station3_torque1": torque_data['station3'].registers[0],
        "station3_torque2": torque_data['station3'].registers[1],
        "station3_torque3": torque_data['station3'].registers[2],
        "station3_status": "OK",

        "station4_torque1": torque_data['station4'].registers[0],
        "station4_torque2": torque_data['station4'].registers[1],
        "station4_torque3": torque_data['station4'].registers[2],
        "station4_status": "OK",
    }

    # Check if part_number already exists
    obj, created = TorqueData.objects.update_or_create(
        part_number=part_number,
        defaults={
            "date": datetime.today().date(),
            "time": datetime.now().time(),
            "shift": shift,
            **station_data
        }
    )
    
    if created:
        logger.info(f"Torque data created for part {part_number}.")
        return f"Torque data created for {part_number}."
    else:
        logger.info(f"Torque data updated for part {part_number}.")
        return f"Torque data updated for {part_number}."
