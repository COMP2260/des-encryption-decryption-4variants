#file name: Bit_manipulation.py
#Description: This file's functions are for the bit string manipulation, including converting string into list of bits, converting bit list back to string,
#converting hexademical to binary, converting binary to hexadecimal value, XOR operation for 2 strings.
#Author: @Nhu Nam Do Nguyen & @Chi Tai Nguyen
#Student ID: c3444589 & c3444339
#Date: 25 May 2025
#Course: COMP3260 - Assignment 2








#convert string input into list
def str_to_bits(s):
    return list(s)

#convert bits to string for output
def bit_to_str(int_list):
    return str(int_list)

#convert hexademical value to interger -> to binary string -> remove 0x
def hex2bin(s):
	return bin(int(s, 16))[2:]

#convert binary to interger -> convert to hexadecimal value -> remove 0x 
def bin2hex(s):
	return hex(int(s,2))[2:].upper()

#convert decimal to binary
def dec2bin(s):
    binary = bin(s)[2:]
    while len(binary) < 4:
        binary = "0" + binary
    return binary
    
#Xor function for 2 strings: a, b
def xor(a,b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result = result + "0"
        else:
            result  = result + "1"
    return result


#final
