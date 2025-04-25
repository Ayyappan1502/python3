import sys
import os
import json
from lib.Argument import Argument
q = Argument(sys.argv)
if(q.hasOptionValue('--file')):
    data = json.loads(os.popen('mediainfo --Output=JSON '+q.getOptionValue('--file')).read())
    if(q.hasCommand('track') and q.hasOptionValue('--type')):
        #if track is in commands and type is in options, return the track of the type
        for i in data['media']['track']:
            if i['@type'] == q.getOptionValue('--type'):
                d = json.dumps(i, indent=4)
                if(q.hasOptionValue('--key')):
                    #if know the key and give for get the value of key
                    print(i[q.getOptionValue('--key')])
                else:
                   
                    
                    if(q.hasOptions(['--key'])):
                         for key in i.keys():
                            print(key)
                    else:
                        print("")
                        print("usage : mediaquerry  [--file] <filename> [--type] <type> [--key]")
                
    else:
        # if(q.hasOption('--file')):
        #     print(json.dumps(data, indent=4))
        # else:  
            print("")
            print("Give the following command..")
            print("[!] : mediaquerry  [--files]=<filename> [--type]=<type> track") 
          
            
    
else:
    if(q.hasOption('--help')):
        q.optionHelper()
    else:
        
        print("Ask : --help for some information (*_*)")