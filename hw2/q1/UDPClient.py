from socket import socket, AF_INET, SOCK_DGRAM

if __name__ == '__main__':
    serverName = 'localhost'
    serverPort = 12001 ## How does the client know???

    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = raw_input('Input sentence: ')
    clientSocket.sendto(message,(serverName, serverPort))
    serverMessage, serverAddress = clientSocket.recvfrom(2048)
    print(serverMessage)
    clientSocket.close()
