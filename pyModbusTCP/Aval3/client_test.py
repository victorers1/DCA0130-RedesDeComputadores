import time
from pyModbusTCP.client import ModbusClient

# Equipamentos no chão de fábrica
nivel0 = 0
nivel1 = 0
nivel2 = 0

c = ModbusClient('172.17.115.225', port=502, unit_id=1)

while True:
    if c.is_open():
        c.write_single_register(0, nivel0)
        c.write_single_register(1, nivel1)
        c.write_single_register(2, nivel2)
        print('nivel0: ' + str(nivel0) + '; nivel1: ' +
              str(nivel1) + '; nivel2: ' + str(nivel2))

        nivel0 = nivel0+2
        nivel1 = nivel1+3
        nivel2 = nivel2+5
    else:
        print('opening client...')
        c.open()
        print('client open!')

    time.sleep(1)
