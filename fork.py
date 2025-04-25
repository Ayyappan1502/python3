import os

r,w= os.pipe()
s = "ayyappan"

if os.fork() == 0:
    print("Child process :"+ str(os.getpid()))
    while True:
        os.write(w, bytes(input('Enter a Text'+': '), 'utf-8'))
 
else:
    print("Parent process :"+ str(os.getpid()))
    while True:
        print("Received message: "+ str(os.read(r, 100),'utf-8'))
 