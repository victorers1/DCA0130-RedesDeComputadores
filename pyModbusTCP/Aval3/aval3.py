import time
from pyModbusTCP.client import ModbusClient

# Equipamentos no chão de fábrica
valvula1 = False
valvula2 = False
nivelTanque1 = 0.0
bracoRobotico = 0

# auto_open=True, auto_close=True
c = ModbusClient(unit_id=1)

c.host("10.13.110.215")
c.port(502)

while True:
    if not c.is_open():
        if not c.open():
            print("conexão falhou")

    on = c.read_coils(6)

    if c.is_open():

        c.write_single_coil(0, valvula1)
        c.write_single_coil(1, valvula2)

        c.write_single_register(2, nivelTanque1)
        c.write_single_register(3, bracoRobotico)
