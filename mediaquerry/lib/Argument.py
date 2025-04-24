class Argument:
    def __init__(self,args):
        self.commands = []
        self.options = []
        self.optionValues = {} #set here
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
 
        
    def hasOptions(self,options:list):
        useroptions = set(self.options)
        requiredOptions = set(options)
        return list(requiredOptions & useroptions)
    
    def hasOption(self,option):
        #if option is in options, return True
        return option in self.hasOptions(option)
    
    def hasOptionValue(self,option):
        #if option is in options, return value
        if option in self.optionValues:
            return True
        else:
            return False
    
    
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
 