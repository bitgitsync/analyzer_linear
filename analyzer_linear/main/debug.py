# -*- coding: utf-8 -*-

class debug_struct:
    
    
    debug = True
    #debug = False
#    def debug(self):
#        pass
#        self.debug = True
#        
#        return self.debug
        
if __name__ == '__main__':
    """
    How to use debug signle
    
    import debug
    debug = debug.debug_struct().debug
    
    """
    pass

    print("Debug state:", debug_struct().debug)
    print (debug_struct().debug)    
    if debug_struct().debug == True:
        pass
        print ("In Debug")
    x = debug_struct()
    print (x.debug)
    
    

