import socket as s
import threading
import select as sel

host = ''
port = 12345
SOCKET_LIST = []

def receive_client():
    server_socket = s.socket(s.AF_INET,s.SOCK_STREAM)
    server_socket.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR)
    server_socket.bind((host,port))
    server_socket.listen()
    SOCKET_LIST.append(server_socket)
    
    while True:
        
        ready_read,ready_write, in_error = sel.select(SOCKET_LIST,[],[],0)
        
        for sock in ready_read :
            if sock == server_socket:
                pass