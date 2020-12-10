from pyModbusTCP.server import ModbusServer
from pynput.keyboard import Listener, Key

# Equipamentos no chão de fábrica
valvula1 = False
valvula2 = False
nivelTanque1 = 0.0
bracoRobotico = 0


def on_press(key):
    global valvula1
    print("Key pressed: {0}".format(key))
    try:
        if key.char == 'v':
            valvula1 = not valvula1
            print("valvula1: " + str(valvula1))
    except:
        print('caractere especial pressionado')


# Create an instance of Listener
with Listener(on_press=on_press) as listener:
    listener.join()


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
