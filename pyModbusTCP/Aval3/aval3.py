from pyModbusTCP.server import ModbusServer
from pynput.keyboard import Listener, Key

val1 = False


def on_press(key):
    global val1
    print("Key pressed: {0}".format(key))
    try:
        if key.char == 'v':
            val1 = not val1
            print("val1: " + str(val1))
    except:
        print('caractere especial pressionado')


# def on_release(key):
    # print("Key pressed: {0}".format(key))
# Create an instance of Listener
with Listener(on_press=on_press) as listener:
    listener.join()


server = ModbusServer('127.0.0.1', port=502, no_block=True)

try:
    server.start()
    print('Server is online')
    while True:
        continue

except:
    server.stop()
    print('Server is offline')


def control(c):
    if c == 1:
        print('abre válvula 1')
    elif c == 2:
        print('abre válvula 2')
