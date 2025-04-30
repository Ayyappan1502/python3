import socket as sock

from threading import Thread

from subprocess import Popen, PIPE, STDOUT
class MathServer(Thread):
    def __init__(self,process,conn):
        Thread.__init__(self)
        self.process = process
        self.conn = conn
    def run(self):
        while not self.process.stdout.closed:
            conn.sendall(self.process.stdout.readline())



host = ''
port = 50002
s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
s.bind((host, port))
s.listen(10)
print('Waiting for connection...')
conn, addr = s.accept()
print('{} Connected by : {} '.format(addr[0],addr[1]))

p = Popen(['bc'], stdout=PIPE, stderr=STDOUT, stdin=PIPE,shell=True)
output_thread = MathServer(p,conn)
output_thread.start()

while not p.stdout.closed:
    data = conn.recv(1024)
    if not data:
        break
    else:
        data = data.decode()
        query = data.strip()
        if query == 'exit' or query == 'quit':
            p.communicate(query.encode(), timeout=1)
            if(p.poll() is not None):
                print('Process terminated')
                break
        query = query+ "\n"
        p.stdin.write(query.encode())
        p.stdin.flush()
            
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