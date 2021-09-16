import can
import asyncio

# Dependencys
# pip3 install python-can python-can-remote
# configure canalyzer config with vector hardware manager to use the VectorCase or the virtual bus
# run on win machine: python -m can_remote -c 0 -i vector
# setup windows ip address and socketcan interface here:
WINDOWS_IP = '192.168.56.1'
SOCKETCAN = 'vcan0'
# run this python script
# 
# The Vector CAN Bus is now connected with your socketcan interface!

async def bridge_bus(bus_source, bus_sink):
    reader = can.AsyncBufferedReader()
    loop = asyncio.get_event_loop()
    notifier = can.Notifier(bus_source, [reader], loop=loop)
    while True:
        msg = await reader.get_message()
        bus_sink.send(msg)


if __name__ == '__main__':
    bus_can = can.interface.Bus(bustype='socketcan', channel=SOCKETCAN)
    bus_ethernet = can.Bus('ws://{}:54701/'.format(WINDOWS_IP),
            bustype='remote',
            bitrate=500000,
            receive_own_messages=False)
    loop = asyncio.get_event_loop()
    loop.create_task(bridge_bus(bus_ethernet, bus_can))
    loop.create_task(bridge_bus(bus_can, bus_ethernet))
    loop.run_forever()
