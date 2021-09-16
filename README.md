# Vector Socketcan Adapter

This is a small helper script to connect a Vector CAN interface or virtual bus to a socketcan interface running on linux machine using ethernet.

The https://github.com/christiansandberg/python-can-remote project is used to tunnel can messages over websockets.

# Usage

- install python on both machines
- install python-can-remote on both machines: `pip3 install python-can-remote`
- on the windows machine
    - start vector hardware configuration
    - configure CAN1 for the CANalyzer application to your interface or virtual bus
    - run python `python -m can_remote -c 0 -i vector`
- on the linux machine
    - change windows ip address and socketcan interface in the python script
    - run `python3 can_bridge_linux.py`
- Gratulations! The Vector CAN Bus and your the socketcan bus are now connected.
