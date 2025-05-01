import socket as sock
from threading import Thread
from subprocess import Popen, PIPE, STDOUT

def start_math_server(conn, addr):
    t = MathServerCommunication(conn,addr)
    t.start()

class ProcesOutThread(Thread):
    def __init__(self,proc,conn):
        Thread.__init__(self)
        self.proc = proc
        self.conn=conn
    def run(self):
        while not self.proc.stdout.closed and not self.conn._closed:
            try:
                self.conn.sendall(self.proc.stdout.readline())
            except:
                pass
        
            
class MathServerCommunication(Thread):
    def __init__(self,conn,addr):
        Thread.__init__(self)
        self.conn=conn
        self.addr=addr
    
    def run(self):
        print("{} connected with back port {}".format(self.addr[0], self.addr[1]))
        self.conn.sendall("Simple Math Server developed by LAHTP \n\nGive any math expressions, and I will answer you :) \n\n$ ".encode())

        p = Popen(['bc'], stdout=PIPE, stderr=STDOUT, stdin=PIPE)
        output_thread = ProcesOutThread(p,self.conn)
        output_thread.start()

        while not p.stdout.closed or not self.conn._closed:
            try:
                data = self.conn.recv(1024)
                if not data:
                    break
                else:
                    try:
                        data = data.decode()
                        query = data.strip()
                        if query == 'quit' or query == 'exit':
                            p.communicate(query.encode(), timeout=1)
                            if p.poll() is not None:
                                break
                        query = query + '\n'
                        p.stdin.write(query.encode())
                        p.stdin.flush()
                    except:
                        pass
            except:
                pass
        self.conn.close()

host = ''
port = 5000

s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
s.setsockopt(sock.SOL_SOCKET, sock.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen()
while True:
    conn, addr = s.accept()
    start_math_server(conn, addr)
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