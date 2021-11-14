DEVICE_NAME = 'GAIT_DATA_LOGGER'

# Bluetooh BLE protocol static UUID
START_UUID = '233ef689-af3f-4ff9-811b-e85f13952409'
PAUSE_UUID = '233ef690-af3f-4ff9-811b-e85f13952409'
RECORD_UUID = '233ef691-af3f-4ff9-811b-e85f13952409'
STOP_UUID = '233ef692-af3f-4ff9-811b-e85f13952409'
BLE_CHARACTERISTICS = [START_UUID, PAUSE_UUID, RECORD_UUID, STOP_UUID]

# Serial Constants
BAUD_RATE = 9600
DEFAULT_PORT = '/dev/ttyACM0'
ACCEL_DATA_HEADERS = ['ax', 'ay', 'az', 'gx', 'gy', 'gz']

TRUE_VAL = bytearray([0x01])
FALSE_VAL = bytearray([0x00])
