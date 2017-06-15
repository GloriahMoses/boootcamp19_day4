class BinarySearch(list):

    def __init__(self, a, b):
        #constrctor method which Initialize the list 
        list.__init__(self)
        self.list_length = a
        self.step = b
        for integer in range(1, a + 1):
            self.append(integer * b) #appending to the list
        self.length = len(self)    #variable assiged to the length of the list    
    
    def search(self, element, bottom=0, top=0, count=0):
    	
        if not top:
        	top = self.length - 1
        if element == self[bottom]:
            return {'index': bottom, 'count': count}
        elif element == self[top]:
            return {'index': top, 'count': count}
        mid = (bottom + top) // 2
        if element == self[mid]:
            return {'index': mid, 'count': count}
        elif element > self[mid]:
            bottom = mid + 1
        elif element < self[mid]:
            top = mid - 1
        if bottom >= top:
            return {'index': -1, 'count': count}
        count += 1  
        return self.search(element, bottom, top, count)
