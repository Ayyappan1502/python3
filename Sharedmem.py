from multiprocessing import shared_memory
from mediaquerry.lib.Argument import Argument
import sys

args = Argument(sys.argv)



if(not args.hasOptions(['--shm', '--ptype'])):
    print('[*] usage : {} --shm=NAME --ptype=[master|slave]'.format(sys.argv[0]))
    
if(args.getOptionValue('--ptype') == 'master'):
    shm = shared_memory.SharedMemory(name=args.getOptionValue('--shm'),create=True , size=1024)

else:
    shm = shared_memory.SharedMemory(name=args.getOptionValue('--shm'))



def writeSHMstring(shm,data):
    
    buf = shm.buf
    
    buf[:len(data)] = bytearray(data, 'utf-8')
    
def readSHMstring(shm):
    buffer = shm.buf
    return str(buffer, 'utf-8').rstrip('\x00')

while(True):
    choice = int(input("1 : Read SHM , 2 : write SHM : choose > "))
    
    if(choice == 1):
       print(readSHMstring(shm))
    elif(choice == 2):
        val = input("Write a string in buffer to SHM : ")
        writeSHMstring(shm,val)
    elif(choice == 0):
        break