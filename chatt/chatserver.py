from socket import *
from chatdatabase import chatRecord
from threading import Thread
import threading
from time import ctime

class clientHandler(Thread):
    def __init__(self, client, record, address):
        Thread.__init__(self)
        self.client = client
        self.record = record
        self.address = address

    def broadCastingMesage(self, activeClient, message):
        for socket in CONNECTION_LIST:
            if socket != server and socket != activeClient:
                try:
                    broadcaseMessage = str.encode(message)
                    socket.send(broadcaseMessage)
                except:
                    print('Client (%s) is offline' %self._address)
                    broadcaseMessage(socket, ("Client ($s) is offline" %self._address))
                    socket.close()
                    CONNECTION_LIST.remove(socket)
    
    def run(self):
        self.client.send(str.encode("Welcome to the chat room!"))
        self.name = bytes.decode(self.client.recv(BUFFER_SIZE))
        allMessage = self.record.getMessage(0)
        self.client.send(str.encode(allMessage))
        while True:
            message = bytes.decode(self.client.recv(BUFFER_SIZE))
            if not message:
                print('Client disconnected')
                self.client.close()
                CONNECTION_LIST.remove(self.client)
                break
            else:
                message = ctime() + ': [' + self.name + ']  -->'  + message
                self.record.addMessage(message)
                threadLock.acquire()
                self.broadCastingMesage(self.client, message)
                threadLock.release()

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 4096
ADDRESS = (HOST, PORT) 
CONNECTION_LIST = []
threadLock = threading.Lock()
record = chatRecord()
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(10)
CONNECTION_LIST.append(server)
print('Chat server started on port %s' %PORT)

while True:
    print('Waiting for connection...')
    client, address = server.accept()
    print('...connected from: ', address)
    threadLock.acquire()
    CONNECTION_LIST.append(client)
    threadLock.release()
    handler = clientHandler(client, record, address)
    handler.start()