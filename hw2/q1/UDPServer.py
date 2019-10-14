from socket import socket, AF_INET, SOCK_DGRAM

if __name__ == '__main__':
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    print('The server is ready to receive')
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)

        # Processing
        modifiedMessage = message.upper()

        print('handled client: ' + str(clientAddress)+ ' who sent: ' + message)
        serverSocket.sendto(modifiedMessage, clientAddress)
