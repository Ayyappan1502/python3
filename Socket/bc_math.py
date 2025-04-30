from threading import Thread

from subprocess import Popen, PIPE, STDOUT
class MathServer(Thread):
    def __init__(self,process):
        Thread.__init__(self)
        self.process = process
    def run(self):
        while not self.process.stdout.closed:
            print(self.process.stdout.readline().decode().rstrip())
p = Popen(['bc', '-q', '-i'], stdout=PIPE, stderr=STDOUT, stdin=PIPE,shell=True)
output_thread = MathServer(p)
output_thread.start()

while not p.stdout.closed:
    query = input('>')
    if query == 'exit' or query == 'quit':
        p.communicate(query.encode(), timeout=1)
        if(p.poll() is not None):
            print('Process terminated')
            break
    query = query+"\n"
    p.stdin.write(query.encode())
    p.stdin.flush()