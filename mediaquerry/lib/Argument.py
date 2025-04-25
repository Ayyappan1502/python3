class Argument:
    def __init__(self,args):
        self.commands = [] #List here
        self.options = []
        self.optionValues = {} #Set here
        self.args = args
   
        for arg in self.args:
            if "-" in  arg:
                #if (-) it is an option or An option with value
                if "=" in arg:
                    pair = arg.split("=")
                    #pair[0] = option, pair[1] = value
                    self.optionValues[pair[0]] = pair[1]
                    #pair[0] is append on options
                    self.options.append(pair[0])
                else:
                    self.options.append(arg)
            else:
                #if not - it is a command or an argument
                self.commands.append(arg)
 
        #simply intersection two value and return them.thus the exection is contribute from hasOption()
    def hasOptions(self,options:list):
        useroptions = set(self.options)
        # print(self.options)
        requiredOptions = set(options)
        # print(options)
        return len(list(requiredOptions & useroptions)) == len(options) # simply return the common value
    
    def hasOption(self,option):
    
        #if option is in options, return True
        return option in self.hasOptions([option])

        #hasOptionValue is value of option.how it is check there , if the option is avaiable in optionValue as true , otherwise false.
    def hasOptionValue(self,option):
        #if option is in options, return value
        if option in self.optionValues:
            return True
        else:
            return False
    
        #simply intersection two value and return them.thus the exection is contribute from hasCommand()
    def hasCommands(self,command:list):
        #if option is in commands, return True
        usercommands = set(self.commands)
        requiredcommand = set(command)
        #simply return the result of the intersection of the two sets
        return list(requiredcommand & usercommands)
    
    def hasCommand(self,command):
        #if option is in commands, return True
        return command in self.hasCommands([command])
    
        #if option is not in options, return default value
    def getOptionValue(self,option , default=None):
    
        #if option is in options, return value
        if option in self.optionValues:
            return self.optionValues[option]
        else:
            return default
        
    def optionHelper(default=None):
        
        print("------------------------------------------------------------------------------------------")
        print("[!] : mediaquerry  [--files]=<filename> [--type]=<type> track [--key]=<key>               |") 
        print(" ")       
        print("[*] --files=<filename> :It is represent the file name for fethch the information          |")
        print("[*] --type=<type>      :It is represent the type of media to gathering the information    |")
        print("[*] --track            :It is represent the track of media                                |")
        print("[*] --key              :It is out all the key from media                                  |")    
        print("[*] --key=<key>        :It is out the value of key from media                             |")
        