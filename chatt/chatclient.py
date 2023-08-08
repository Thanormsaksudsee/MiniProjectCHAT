from socket import *

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 4096
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
messageFromServer = bytes.decode(server.recv(BUFFER_SIZE))
print(messageFromServer)
name = input('Enter your name: ')
userName = str.encode(name)
server.send(userName)

while True:
    receiveMessage = bytes.decode(server.recv(BUFFER_SIZE))
    if not receiveMessage:
        print('Server disconnected')
        break
    print(receiveMessage)
    sendMessage = input('Enter your message: ')
    if not sendMessage:
        print('Server disconnected')
        break
    server.send(str.encode(sendMessage))

server.close()