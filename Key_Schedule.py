'''
File Name: Key_Schedule.py
'''


from DES_Components import PC1, PC2

#shift left:
def shift_left(k, pos): 
    return k[pos:] + k[:pos] #move the first n bit to the end

#apply pc1
def apply_pc1(s):
    result = ""
    for i in range(len(PC1)):
        result = result + s[PC1[i] -1]

    return result

#split key 
def split_key(s):
    #split 56-bit key into two 28-bit key halves
    return [s[:28], s[28:]]


#apply pc2
def apply_pc2(s):
    result = ""
    for i in range(len(PC2)):
        result = result + s[PC2[i]-1]
    return result
