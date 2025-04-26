#! usr/bin/python3

print("git hub is updated successfully :)")
import os
#execute the command through os module in popen() ,
# therefore it simply read the output from cmd prompt 
# And deliver the output via python exection , that is happened at behind the scene.
output = os.popen('ls').read()
print(output)