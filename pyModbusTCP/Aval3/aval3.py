from pyModbusTCP.server import ModbusServer
from pynput.keyboard import Listener, Key

# Equipamentos no chão de fábrica
valvula1 = False
valvula2 = False
nivelTanque1 = 0.0
bracoRobotico = 0


# auto_open=True, auto_close=True
server = ModbusServer('127.0.0.1', port=520, no_block=True)

try:
    server.start()
    print('Server is online')
    while True:

        continue  # TODO: envio dos estados para SCADA


except:
    server.stop()
    print('Server is offline')
