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

#initital permutation
def permute(s, table):
    permutation = ""
    for i in range(0, len(table)):
        permutation += s[table[i] -1] #as python is 0-based indexing
    
    return permutation
#final
