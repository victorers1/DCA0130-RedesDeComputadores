import time
from pyModbusTCP.client import ModbusClient

# Equipamentos no chão de fábrica
valvula1 = False
valvula2 = False
nivelTanque1 = 0.0
bracoRobotico = 0

# auto_open=True, auto_close=True
c = ModbusClient()

c.host("172.17.115.225")
c.port(502)

while True:
    if not c.is_open():
        if not c.open():
            print("conexão falhou")

    # on = c.read_coils(4)

    if c.is_open():
        c.write_single_coil(0, valvula1)
