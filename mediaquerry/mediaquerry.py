import sys
import os
import json
from lib.Argument import Argument
q = Argument(sys.argv)
if(q.hasOptionValue('--files')):
    data = json.loads(os.popen('mediainfo --Output=JSON '+q.getOptionValue('--files')).read())
    if(q.hasCommand('track') and q.hasOptionValue('--type')):
        #if track is in commands and type is in options, return the track of the type
        for i in data['media']['track']:
            if i['@type'] == q.getOptionValue('--type'):
                d = json.dumps(i, indent=4)
                if(q.hasOptionValue('--key')):
                    print(i[q.getOptionValue('--key')])
                else:
                    # print("unable to fetch the value , provide keys what you want to fetch")
                    
                    if(q.hasOptions(['--key'])):
                         for key in i.keys():
                            print(key)
                    else:
                        print("doesn't exist the key in options..")
                
    else:
        print(json.dumps(data, indent=4))
    
else:
    print("No Files , Please provide a file using --files=<file>")
