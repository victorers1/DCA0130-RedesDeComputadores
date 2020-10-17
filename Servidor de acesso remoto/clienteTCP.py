# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Cliente de sockets TCP modificado para enviar texto minusculo ao servidor e aguardar resposta em maiuscula (python 3)
#

# importacao das bibliotecas
from socket import *

serverName = 'localhost' 
serverPort = 61000 
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName, serverPort)) 

sentence = input('Digite um comando: ')

clientSocket.send(sentence.encode('utf-8')) 

modifiedSentence = clientSocket.recv(1024) 

print('O servidor (\'%s\', %d) respondeu com: %s' %
      (serverName, serverPort, modifiedSentence.decode('utf-8')))
      
clientSocket.close() 
