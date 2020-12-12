import time
from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep

server = ModbusServer("172.17.115.225", 502, no_block=True)

try:
    while True:
        print("Iniciando servidor...")
        server.start()
        print("Servidor iniciado")

        while True:
            DataBank.get_words(0)
            DataBank.get_words(1)
            DataBank.get_words(2)
            sleep(1)

except:
    print("Desligando servidor...")
    server.stop()
    print("Servidor desligado")
