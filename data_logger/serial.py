from os import execlpe
import serial
from data_logger.constant import BAUD_RATE, DEFAULT_PORT


class SerialLogger:
    baud_rate = BAUD_RATE
    serial_port = DEFAULT_PORT
    ser = None

    def __init__(self):
        ser = serial.Serial(self.serial_port, self.baud_rate)
        ser.flushInput()

    def decode_bytes(self, data):
        return str(data[0:len(data) - 2]).decode("utf-8")

    def read_serial(self):
        try:
            bytes = self.ser.readline()
            decoded_bytes = self.decode_bytes(bytes)
            return decoded_bytes
        except KeyboardInterrupt as e:
            raise e
