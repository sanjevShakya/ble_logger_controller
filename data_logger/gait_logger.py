from bleak import BleakClient
from data_logger.constant import FALSE_VAL, START_UUID, PAUSE_UUID, RECORD_UUID, STOP_UUID, TRUE_VAL
from data_logger.constant import BLE_CHARACTERISTICS


class GaitLogger:
    client = None
    states = {
        [START_UUID]: True,
        [PAUSE_UUID]: False,
        [RECORD_UUID]: False,
        [STOP_UUID]: False,
    }

    def __init__(self, bleClient: BleakClient):
        self.client = bleClient
        self.handler_map = {
            START_UUID: self.handle_start,
            PAUSE_UUID: self.handle_pause,
            STOP_UUID: self.handle_stop,
            RECORD_UUID: self.handle_record,
        }

    def get_bool_val(on):
        if on:
            return TRUE_VAL
        else:
            return FALSE_VAL

    async def read_state(self, characteristic):
        val = await self.client.read_gatt_char(characteristic)
        return val

    async def write_state(self, uuid, val):
        val = await self.client.write_gatt_char(uuid, self.get_bool_val(val))
        return True

    async def update_states(self):
        # val = await self.client.read_gatt_char(characteristic)
        for uuid in self.states:
            self.write_state(uuid, self.states[uuid])

    async def set_state():
        pass

    async def listen_topics(self):
        await self.update_states()

        while True:

            await self.set_state()
