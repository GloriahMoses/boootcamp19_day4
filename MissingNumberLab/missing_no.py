def find_missing(list_1,list_2):
    """This function finds the missing number in one of the given 
    two lists and returns respective output"""
    
    if list_1 ==[] and list_2==[]: #if lists are empty a 0 is returned
        return 0
    elif (list_1) == (list_2):
        return 0
    else: #check for number not in both lists
        for number in list_1:
            if number not in list_2:
                return number   
        for number in list_2: 
            if number not in list_1:
                return number
