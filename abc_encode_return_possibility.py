# 'a' - > 1, 'b' -> 2,....,'z'->26
#data_input = 12, o/p in this case can be 'ab', 'l'
#data_input = 123, abc
#parse the input [1,2,12], {('a':1),('b':2),..,('l':12)}

def createLetterMap():
    letter_map={}
    value=1
    #this can be its own subroutine O(n)
    for i in range(ord('a'),ord('z')+1):
        letter_map.update({chr(i):value})
        #increment value
        value +=1
    return (letter_map)
def getLetterCombination(input_data):
    #parse input data to individual numbers and single
    parse_input=[]
    for idx in str(input_data):
        parse_input.append(int(idx))
    if len(str(input_data))==2:
        parse_input.append(input_data)
    letter_combination=[]
    letter_map=createLetterMap()
    ret_string=str()
    for key,val in letter_map.items():
        for input in parse_input:
            if len(str(val))==2 and val==input:
               letter_combination.append(key)
            elif val==input:
               ret_string=ret_string+str(key)
    if ret_string:           
        letter_combination.append(ret_string)
    if not letter_combination:
        letter_combination.append('0')
    return(letter_combination)
input_data=26
res=getLetterCombination(input_data)
print(res)