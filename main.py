from DES_IMPLEMENTATION import *
from Bit_manipulation import *
from Key_Schedule import *

def main():
    P, P_1, K, K_1 = 0 #read input file
    ciphertext = encrypt(P, K)

    #avalance analysis
    result = #avalanche_analysis(P, P_1, K, K_1)




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
