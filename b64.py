import sys
import base64 

if(len(sys.argv) != 3 and sys.argv[2] == "-h" or "--help"):
    # It is represent the requirement parameter..{-e|-d}
    print("usage : md5  {-e|-d} [-h] \"<string>\"")    
    print(" -e | encode the data")
    print(" -d | decode the data")
 
    exit
    
option = sys.argv[1]

if (option == "-e"):
    #sys.argv[2] is data 
    #encode() is directly convert byte code 
    #decode() is convert to b64 from byte code
    print(base64.b64encode(sys.argv[2].encode()).decode())
elif(option == "-d"):
    print(base64.b64decode(sys.argv[2].encode()).decode())
