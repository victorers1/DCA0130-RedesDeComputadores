import time
from pyModbusTCP.client import ModbusClient
from pynput.keyboard import Listener, Key

# Equipamentos no chão de fábrica
valvula1 = False
valvula2 = False
nivelTanque1 = 0.0
bracoRobotico = 0

# auto_open=True, auto_close=True
c = ModbusClient('172.18.66.225', port=502, unit_id=1)

while True:
    if c.is_open():
        c.write_single_coil(0, 1)
        c.write_single_coil(1, 1)
        c.write_single_coil(2, 1)
        c.write_single_coil(3, 1)
        print('enviado!')
    else:
        print('opening client...')
        c.open()
        print('client open!')

    time.sleep(1)
