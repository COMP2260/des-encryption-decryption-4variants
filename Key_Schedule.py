'''
File Name: Key_Schedule.py
Description: Performs key functions, including: 
- shift_left: shift the position of the key by number of bit k
- apply_pc1: apply the pc1 table into the bit string
- apply_pc2: apply the pc2 table into the bit string
- split_key: split 56-bit key into two 28-bit keys
Author: @Nhu Nam Do Nguyen @Chi Tai Nguyen
Student ID: c3444589 & c3444339
Date: 30 May 2025
Course: COMP3260 - Assignment 2
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
