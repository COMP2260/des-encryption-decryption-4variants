from DES_IMPLEMENTATION import *
from Bit_manipulation import xor

def f_function(r32, round_key, version='DES0'): #default if des0
    if len(r32) != 32:
        raise ValueError("Input should be 32-bit long")
    expand = expand_perm(r32)

    #check DES type
    if version == 'DES1':
        input1  = expand    # skip XORing with round key
    else:
        input1 = xor(expand, round_key)

    if version == 'DES2':
        sub = inverse_expand(input1) # perform inverse expansion
    else:
        sub = apply_sbox(input1)

    if version == 'DES3':
        return sub  # skip P permutation
    else:
        return perm_P(sub) 
