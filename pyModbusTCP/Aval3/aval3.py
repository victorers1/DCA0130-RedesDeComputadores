from pyModbusTCP.server import ModbusServer

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
