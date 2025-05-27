#initial permutation
def initial_perm(s):
    #check if the input is exact 64-bit
    if len(s) != 64:
        raise ValueError("The input must be 64-bit")
    result = ""
    for i in range(len(IP)):
        result = result + s[IP[i] -1]
    
    return result

#inverse permutation
def inverse_perm(s):
    #check input length
    if len(s) != 64:
        raise ValueError("The input must be 64-bit")
    result = ""
    for i in range(len(I_IP)):
        result = result + s[I_IP[i] - 1]
    
    return result

#expansion permutation
def expand_perm(s):
    #check the input length is 32-bit
    if len(s) != 32:
        raise ValueError("The input must be 32-bit")
    
    result = ""
    for i in range(E):
        result = result + s[E[i] - 1]
    return result
    
def inverse_expand(s):
    return 0
#permutation P
def perm_P(s):
    if len(s) != 32:
        raise ValueError("The input must be 32-bit")
    result = ""

    for i in range(P):
        result = result + s[P[i] -1 ]
    return result

#apply sboxes
def apply_sbox(s):
    if len(s) != 48:
        raise ValueError("The input must be exactly 48 bits")
    result = ""
    for i in range(8):
        #split into 6-bit blocks
        block = s[i*6:(i+1)*6]
        row = int(block[0] + block[5], 2) #convert binary -> decimal with int()
        column = int(block[1:5], 2)
        val = S_BOXES[i][row][column]
        result = result + dec2bin(val)
    return result

