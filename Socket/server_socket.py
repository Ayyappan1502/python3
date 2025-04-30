import socket as s
import threading
import sys
import select as sel

"""
step 1: import modules like socket, threading, select
step 2: create a socket object for receiving clients 
step 3: setsockopt to reuse the address which i has used socket layer ,reuse address attribute in socket
step 4: bind the socket to the host and port
step 5: listen for incoming connections
step 6: create a list of sockets to be monitored for incoming connections
step 7: create a while loop to accept incoming connections and handle them in a separate thread
    
"""

host = 'localhost' #localhost =
port = 4444
SOCKET_LIST = []
RECEIVE_BUFF = 1024 #buffer size for receiving data

def chat_Server():
    server_socket = s.socket(s.AF_INET,s.SOCK_STREAM) #inet = ipv4, sock_stream = tcp
    server_socket.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1) #reuse the address
    server_socket.bind((host,port))# #bind the socket to the host and port
    server_socket.listen()# #listen for incoming connections
    SOCKET_LIST.append(server_socket) #add the server socket to the list of sockets to be monitored for incoming connections
    
    while True:
        # Use select to wait for incoming connections
        # The select function will block until there is an incoming connection or a timeout occurs
        ready_read,ready_write, in_error = sel.select(SOCKET_LIST,[],[])
        
        for sock in ready_read :
                if sock == server_socket:
                # Accept a new connection
                    sockfd, addr = server_socket.accept()
                    SOCKET_LIST.append(sockfd) #add the new socket to the list of sockets to be monitored for incoming connections
                    print("Connection from {}:{} has been established!".format(addr[0],addr[1]))
                    broadcast(server_socket,sockfd, "[{}] entered the chat room\n".format(addr)) #broadcast a message to all clients except the server socket and the client socket
                else:
                    try:
                        data = sock.recv(RECEIVE_BUFF) #receive data from the socket
                        data = data.decode() #decode the data received from the socket
                        if data:
                            broadcast(server_socket,sockfd, "[{}] {} entered the chat room\n".format(sock.getpeername(),data))
                        else:
                            # If data is not received, it means the client has disconnected
                            broadcast(server_socket,sockfd, "[{}]  {} entered the chat room\n".format(sock.getpeername(),"disconnected"))
                            if sock in SOCKET_LIST:
                                SOCKET_LIST.remove(sock) #remove the socket from the list of sockets to be monitored for incoming connections
                                print(f"Client {sock.getpeername()} has disconnected.")
                    except Exception as e:
                        broadcast(server_socket,sockfd, "[{}]  {} ".format(sock.getpeername(),"client has disconnected"))
                        continue
                    except KeyboardInterrupt:
                        print("Server exiting...")
                        server_socket.close()
                        sys.exit()
print("Server listening...")
        # server_socket.close() #close the server socket
        # print("Server socket closed.")
        
    
def broadcast(server_socket,client_socket, message):
    for socket in SOCKET_LIST:
        if socket != server_socket and socket != client_socket:
            try:

                socket.send(message.encode()) #send the message to all clients except the server socket and the client socket
            except Exception as e:
                socket.close() #close the socket if there is an error
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)#remove the socket from the list of sockets to be monitored for incoming connections
if __name__ == "__main__":
    sys.exit(chat_Server()) #call the chat server function to start the server
     