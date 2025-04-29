import sys
import socket as s
import threading
import select as sel

SOCKET_LIST = [] #list of sockets to be monitored for incoming connections
REEIVE_BUFF = 1024 #buffer size for receiving data
host = sys.argv[1]
port = int(sys.argv[2])

def chat_Client():
    if len(sys.argv) != 3:
        print("Usage: python {} <hostname> <port>".format(sys.argv[0]))
    host = sys.argv[1]
    port = int(sys.argv[2])

    client_socket = s.socket(s.AF_INET,s.SOCK_STREAM) #inet = ipv4, sock_stream = tcp
    client_socket.settimeout(5) #set a timeout for the socket
    try:
        client_socket.connect((host,port)) #connect to the server
    except:
        print("Error connecting to server: {} : {}".format(host,port))
        sys.exit(-1)
    print("Connected to server at {}:{}".format(host,port))
    SOCKET_LIST.append(client_socket) #add the client socket to the list of sockets to be monitored for incoming connections
    SOCKET_LIST.append(sys.stdin) #add the standard input to the list of sockets to be monitored for incoming connections
    sys.stdout.write("> ") #prompt the user for input
    sys.stdout.flush() #flush the output buffer to ensure that the prompt is displayed immediately
        
    while True:
        read_ready,write_ready, in_error = sel.select(SOCKET_LIST, [], []) #create a list of sockets to be monitored for incoming connections
        # # Use select to wait for incoming messages
        for sock in read_ready:
            try:
                if sock == client_socket: # If the socket is the client socket, it means it is a new message from the server
                    data = sock.recv(REEIVE_BUFF) #receive data from the socket
                    if not data:
                        print("Disconnected from server.")
                        sys.exit()
                    else:
                        sys.stdout.write(data.decode()) #decode the data received from the socket
                        sys.stdout.write("> ")
                        sys.stdout.flush() 
        
                else:# If the socket is not the client socket, it means it is a new message from the server
                    message = sys.stdin.readline()
                    client_socket.send(message.encode())
                    sys.stdout.write("> ")
                    sys.stdout.flush()
            except KeyboardInterrupt :
                print("Client exiting...")
                client_socket.close()
                sys.exit()
        
        
if __name__ == "__main__":
    sys.exit(chat_Client()) #call the chat client function to start the client
    