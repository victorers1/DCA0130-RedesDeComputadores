# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets TCP modificado para receber texto minusculo do cliente enviar resposta em maiuscula  (python 3)
#

# importacao das bibliotecas
from socket import *  # sockets
import time

# definicao das variaveis
serverName = ''  # ip do servidor (em branco)
serverPort = 61000  # porta a se conectar
serverSocket = socket(AF_INET, SOCK_STREAM)  # criacao do socket TCP
# bind do ip do servidor com a porta
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)  # socket pronto para 'ouvir' conexoes
print('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    connectionSocket, addr = serverSocket.accept()  # aceita as conexoes dos clientes
    sentence = connectionSocket.recv(1024)  # recebe dados do cliente
    sentence = sentence.decode('utf-8')
    if 'obter' in sentence:
        try:
            file = open(sentence.split(' ')[1])
            response = file.read()
        except:
            response = 'Arquivo não existe'
    else:
        response = 'Comando desconhecido'
        
    connectionSocket.send(response.encode('utf-8'))
    connectionSocket.close()  # encerra o socket com o cliente
serverSocket.close()  # encerra o socket do servidor
