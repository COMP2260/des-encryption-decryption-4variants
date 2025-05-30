'''
File Name: DES_IMPLEMENTATION.py

Description:
    The functions in this file will be implemented based on the initialized tables
    in DES_Components with the decimal to binary (dec2bin) conversion function from 
    Bit_manipulation for the S-boxes. The functions include:
    * initial_perm(s): apply IP table transformation to input s, which is a 64-bit string.
    * inverse_perm(s): apply the inverse IP table transformation to input s, which is a 64-bit string.
    * expand_perm(s): apply the E table transformation to input s, which is a 32-bit string.
    * inverse_expand(s): apply the inverse E table transformation to input s, which is a 48-bit string.
    * perm_P(s): apply the P table transformation to input s, which is a 32-bit string.
    * apply_sbox(s): applies the S-boxes to the input s, which is a 48-bit string.

Author: @Nhu Nam Do Nguyen @Chi Tai Nguyen

Student ID: c3444589 & c3444339

Date: 30 May 2025

Course: COMP3260 - Assignment 2
'''

from DES_Components import *
from Bit_manipulation import dec2bin

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
    for i in range(len(E)):
        result = result + s[E[i] - 1]
    return result

# inverse expansion
def inverse_expand(s):
    # check that the input length is 48-bit
    if len(s) != 48:
        raise ValueError("The input must be 48-bit")

    # convert E to 0-based indexing
    E_zero_based = [e - 1 for e in E]

    # creating a reverse mapping from E
    E_reverse = [[] for i in range(32)]
    for i, src, in enumerate(E_zero_based):
        E_reverse[src].append(i)
        # this will determine which bit positions of s are duplicates
        # Format: [[1, 47], [2, 48], [3], [4, 6], ...]
        # Each sublist's index corresponds to the original, pre-expandPerm() bit position

    result = ""
    for i in range(32):
        result = result + s[E_reverse[i][0]]     # take the first entry
    return result

#permutation P
def perm_P(s):
    if len(s) != 32:
        raise ValueError("The input must be 32-bit")
    result = ""

    for i in range(len(P)):
        result = result + s[P[i] - 1]
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

