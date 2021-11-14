import asyncio
from data_logger.ble_client import BleClient

device_name = 'GAIT_DATA_LOGGER'


async def program():
    ble_client = None
    bleak_client = None
    loop = asyncio.get_running_loop()

    def app(client):
        nonlocal bleak_client
        bleak_client = client
        
        print('app callback called')
        pass

    try:
        ble_client = BleClient(device_name, app)
        loop.run_in_executor(None, await ble_client.run())

    except KeyboardInterrupt:
        print('\nReceived keyboard interrupt')
    finally:
        if ble_client.client:
            print("Disconnecting...")
            await ble_client.client.disconnect()
        print("Exit")


def main():
    asyncio.run(program())
