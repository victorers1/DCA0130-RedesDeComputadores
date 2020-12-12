#!/usr/bin/env python
# -*- coding: utf-8 -*-

# importacao das bibliotecas
from pyModbusTCP.client import ModbusClient

# define o cliente
c = ModbusClient()

# debug do cliente
#c.debug(True)

# ip/porta do servidor modbus (para se conectar)
c.host("10.13.110.215")
c.port(502)

while True:
    # para abrir a conexao TCP com o servidor
    if not c.is_open():
        if not c.open():
            print ("unable to connect")
    
    # read_coils() para leitura de dados vindo do servidor/supervisorio
    on = c.read_coils(6)

    # se a conexao estabelecida, entao escreve (write coils (modbus function 0x01))
    if c.is_open():
        
        c.write_single_coil(v1, valvula1)
        c.write_single_coil(v2, valvula2)

        c.write_single_register(n1, nivel1)
        c.write_single_register(n2, nivel2)
        
        # ... logica de codigo a implementar de acordo com a aplicacao a ser desenvolvida
