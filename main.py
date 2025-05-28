from DES_IMPLEMENTATION import *
from Bit_manipulation import *
from Key_Schedule import *

def encrypt(plaintext, key, mode='DES0'):
    plaintext = hex2bin(plaintext)

    # Perform Initial Permutation (IP)
    plaintext = initial_perm(plaintext)

    # Split plaintext into left and right halves
    left = plaintext[0:32]
    right = plaintext[32:64]

    # Perform Permutated Choice 1 transformation on master key
    key = apply_pc1(key)

    # Split master key into left and right halves
    C, D, firstKeySplit = list(), list(), split_key(key)
    C.append(firstKeySplit[0])
    D.append(firstKeySplit[1])

    # Perform Feistel rounds
    for i in range(16):
        # Expand the right half of the plaintext from 32 to 48-bit
        right_expanded = expand_perm(right)



if __name__ == '__main__':

    key = "0111001101110101011100110110100001101001011100100110010101110110"
    splits = split_key(apply_pc1(key))
    print(splits, len(splits[0]))
    print(bin2hex(key))
    # Etest = expand_perm(test)
    # IEtest = inverse_expand(Etest)
    # print("Etest = expand_perm(test):", Etest, ". String length: ", len(Etest), sep="")
    # print("inverse_expand(Etest): ", IEtest, "\ntest: ", test, "\nEqual string length: ", len(IEtest) == len(test),
    #       "\nExact match: ", IEtest == test, sep='')