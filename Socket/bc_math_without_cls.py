import threading
import time
from subprocess import Popen, PIPE, STDOUT

p = Popen(['bc','-i'], stdout=PIPE, stderr=PIPE, stdin=PIPE,shell=True)

def read_threat(p):
    while p.poll() is None:
        print(p.stdout.readline().decode(), end='')
        
t = threading.Thread(target=read_threat, args=(p,))
t.start()
        

while p.poll() is None:
    query = input("bc_math $: ")
    if query == 'exit' or query == 'quit':
        p.communicate(query.encode(), timeout=1)
        if(p.poll() is not None):
            print('Process terminated')
            break
    query = query+ "\n"
    p.stdin.write(query.encode())
    p.stdin.flush()
    
    