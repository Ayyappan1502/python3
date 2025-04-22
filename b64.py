import sys
import base64 

if(len(sys.argv) != 3):
    print("usage : md5  {-e|-d}\" <string>\"n")
    exit




option = sys.argv[1]

if (option == "-e"):
    print(base64.b64encode(sys.argv[2].encode()).decode())
elif(option == "-d"):
    print(base64.b64decode(sys.argv[2].encode()).decode())
