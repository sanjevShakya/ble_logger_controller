import asyncio
from bleak import BleakClient
from bleak import discover


class BleClient:
    device_name = ''
    found = False
    connected = False
    client = None
    devices = []

    def __init__(self, device_name, app_cb):
        self.device_name = device_name
        self.app_cb = app_cb
        pass

    async def handle_device_found(self, device):
        print('Found {}'.format(self.device_name))
        self.found = True
        self.connected = False
        print(device)
        async with BleakClient(device.address) as client:
            print(f'Connected to {device.address}')
            self.client = client
            self.connected = True
            self.app_cb(client)
        pass

    async def run(self):
        print('Looking for Arduino NANO BLE Device')
        print('{} Device...'.format(self.device_name))
        self.found = False
        devices = await discover()
        for d in devices:
            if self.device_name in d.name:
                await self.handle_device_found(d)
        if not self.found:
            print("Cound not find {}".format(self.device_name))
