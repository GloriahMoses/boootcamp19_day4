class BinarySearch(list):
    
    def __init__(self, a, b):
        #Initialize list function
        list.__init__(self)
        self.list_length = a
        self.step = b
        for integer in range(1, a + 1):
            self.append(integer * b) #appending to the list
        self.length = len(self)    #variable assiged to the length of the list    
    
